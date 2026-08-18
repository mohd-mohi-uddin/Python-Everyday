from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
from pathlib import Path


# Get the folder where this Python file is located
BASE_DIR = Path(__file__).parent


# Login credentials for the gym website
ACCOUNT_EMAIL = "mohiuddin@test.com"
ACCOUNT_PASSWORD = "mohiuddin@14"

# Website URL
GYM_URL = "https://appbrewery.github.io/gym/"


# ==================================================
# CHROME SETUP
# ==================================================

# Create Chrome options so we can customize the browser
chrome_options = webdriver.ChromeOptions()

# Keep Chrome open after the program finishes
chrome_options.add_experimental_option("detach", True)

# Create the path for our separate Chrome profile
user_data_dir = os.path.join(BASE_DIR, "chrome_profile")

# Print the profile location
print(user_data_dir)

# Tell Chrome to use this folder as its profile
# This allows Chrome to remember login/session data
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


# Open Chrome using our custom options
driver = webdriver.Chrome(options=chrome_options)

# Open the gym website
driver.get(GYM_URL)


# ==================================================
# WAIT SETUP
# ==================================================

# Create an explicit wait with a maximum wait time of 10 seconds
wait = WebDriverWait(driver, 10)


# ==================================================
# LOGIN
# ==================================================

# Wait until the login button becomes clickable
login_button = wait.until(
    ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="home-page"]/section[1]/div/div/a[1]/button')
    )
)

# Click the login button
login_button.click()


# Wait until the email input exists on the page
enter_email = wait.until(
    ec.presence_of_element_located(
        (By.XPATH, '//*[@id="email-input"]')
    )
)

# Clear anything already inside the email field
enter_email.clear()

# Enter the account email
enter_email.send_keys(ACCOUNT_EMAIL)


# Find the password field
enter_password = driver.find_element(
    By.XPATH,
    '//*[@id="password-input"]'
)

# Clear the password field
enter_password.clear()

# Enter the account password
enter_password.send_keys(ACCOUNT_PASSWORD)


# Find the login/submit button
press_login = driver.find_element(
    By.XPATH,
    '//*[@id="submit-button"]'
)

# Click the login button
press_login.click()


# ==================================================
# WAIT FOR THE SCHEDULE PAGE
# ==================================================

# Wait until the schedule page exists
wait.until(
    ec.presence_of_element_located(
        (By.ID, "schedule-page")
    )
)


# ==================================================
# COUNTERS
# ==================================================

# Count new bookings
bookings = 0

# Count new waitlists joined
waitlists = 0

# Count classes that were already booked or waitlisted
already_booked_or_waitlisted = 0

# Count total matching Tuesday 6 PM classes processed
total_processed = 0


def book_class(day):

    # ==================================================
    # FIND THE 6 PM CLASS for the given day
    # ==================================================

    # Find all <p> elements whose ID starts with "class-time-"
    class_times = driver.find_elements(
        By.CSS_SELECTOR,
        "p[id^='class-time-']"
    )

    global bookings, waitlists, already_booked_or_waitlisted, total_processed
    # Loop through every class time found on the page
    for class_time in class_times:

        # Move upward through the HTML hierarchy
        # until we reach the day group containing this class
        parent = class_time.find_element(
            By.XPATH,
            "./../../../.."
        )

        # Check:
        # 1. The class belongs to Thursday
        # 2. This particular class is at 6:00 PM
        if day in parent.text and "6:00" in class_time.text:

            # We found a matching class
            total_processed += 1

            # Move upward from the time element to its class card
            class_details_path = class_time.find_element(
                By.XPATH,
                "./../../.."
            )

            # Find the button inside this particular class card
            book_button = class_details_path.find_element(
                By.TAG_NAME,
                value="button"
            )


            # ==================================================
            # CHECK BOOKING STATUS
            # ==================================================

            button_status = book_button.text

            # Only click if the class isn't already booked
            # or already on the waitlist
            if book_button.text != "Booked" and book_button.text != "Waitlisted":
                book_button.click()


            # ==================================================
            # GET CLASS DETAILS
            # ==================================================

            # Find the day title inside the day group
            date = parent.find_element(
                By.CLASS_NAME,
                "Schedule_dayTitle__YBybs"
            )

            # Find the class name inside the class card
            class_name = class_details_path.find_element(
                By.TAG_NAME,
                value="h3"
            )


            # ==================================================
            # UPDATE COUNTERS + PRINT MESSAGE
            # ==================================================

            if button_status == "Waitlisted":

                # Already on the waitlist
                already_booked_or_waitlisted += 1

                print(
                    f"✓ Already on waitlist: "
                    f"{class_name.text} on {date.text}"
                )

            elif button_status == "Join Waitlist":

                # Successfully joined the waitlist
                waitlists += 1

                print(
                    f"✓ Joined waitlist for: "
                    f"{class_name.text} on {date.text}"
                )

            elif button_status == "Booked":

                # Already booked
                already_booked_or_waitlisted += 1

                print(
                    f"✓ Already booked: "
                    f"{class_name.text} on {date.text}"
                )

            else:

                # Successfully made a new booking
                bookings += 1

                print(
                    f"✓ Booked: "
                    f"{class_name.text} on {date.text}"
                )

book_class(day="Thu")
book_class(day="Fri")


# ==================================================
# BOOKING SUMMARY
# ==================================================

print("\n--- BOOKING SUMMARY ---")
print(f"Classes booked: {bookings}")
print(f"Waitlists joined: {waitlists}")
print(f"Already booked/waitlisted: {already_booked_or_waitlisted}")
print(f"Total 6pm classes processed: {total_processed}")


#Close the browser
driver.close()
