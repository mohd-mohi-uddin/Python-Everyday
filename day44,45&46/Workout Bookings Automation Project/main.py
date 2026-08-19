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


# CHROME SETUP

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


# WAIT SETUP
# Create an explicit wait with a maximum wait time of 10 seconds
wait = WebDriverWait(driver, 10)



# COUNTERS
# Count total matching Tuesday 6 PM classes processed
total_processed = 0



# LOGIN
def login():

    # Open the gym website
    driver.get(GYM_URL)

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

    print("Login button clicked. Waiting for schedule page...")

    # WAIT FOR THE SCHEDULE PAGE

    # Wait until the schedule page exists
    wait.until(
        ec.presence_of_element_located(
            (By.ID, "schedule-page")
        )
    )


def book_class(day):

    # FIND THE 6 PM CLASS for the given day
    
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

            # CHECK BOOKING STATUS
            
            button_status = book_button.text

            # Only click if the class isn't already booked
            # or already on the waitlist
            if book_button.text != "Booked" and book_button.text != "Waitlisted":
                book_button.click()

            # GET CLASS DETAILS
        
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

            #PRINT MESSAGE
            
            if button_status == "Waitlisted":

                print(
                    f"✓ Already on waitlist: "
                    f"{class_name.text} on {date.text}"
                )

            elif button_status == "Join Waitlist":

                print(
                    f"✓ Joined waitlist for: "
                    f"{class_name.text} on {date.text}"
                )

            elif button_status == "Booked":

                print(
                    f"✓ Already booked: "
                    f"{class_name.text} on {date.text}"
                )

            else:

                print(
                    f"✓ Booked: "
                    f"{class_name.text} on {date.text}"
                )

    print(f"\nbook_class() worked for {day}\n")

def retry(func, retries=7, description=None):

    for attempt in range(retries):

        try:
            func()
            return True

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {type(e).__name__}: {e}")

    return False

login_success = retry(login)

if not login_success:
    print("❌ Login failed after all retries.")
    driver.quit()
    exit()

thursday_success = retry(lambda: book_class(day="Thu"))
if not thursday_success:
    print("❌ failed to book a class.")
    driver.quit()
    exit()

saturday_success = retry(lambda: book_class(day="Sat"))
if not saturday_success:
    print("❌ failed to book a class.")
    driver.quit()
    exit()
# # BOOKING SUMMARY

print(f"Total Tuesday/Thursday 6pm classes: {total_processed}")

#verifing on my bookings page

my_bookings_button = driver.find_element(By.XPATH, value='//*[@id="my-bookings-link"]')
my_bookings_button.click()

count_of_bookings = wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="my-bookings-page"]')))
booked_count =count_of_bookings.get_attribute("data-bookings-count")
waitlisted_count = count_of_bookings.get_attribute("data-waitlist-count")
total_bookings = int(booked_count) + int(waitlisted_count)

print("--- VERIFYING ON MY BOOKINGS PAGE ---")
print(f"✓ Verified: {booked_count} booked class")
print(f"✓ Verified: {waitlisted_count} class in Waitlist")

if total_bookings == total_processed:
    print("--- VERIFICATION RESULT ---")
    print(f"Expected: {total_processed} bookings")
    print(f"Found: {total_bookings} bookings")
    print("✅ SUCCESS: All bookings verified!")

else:
    print("--- VERIFICATION RESULT ---")
    print(f"Expected: {total_processed} bookings")
    print(f"Found: {total_bookings} bookings")
    print("! ERROR: found less bookings then Expected")    


#Close the browser
driver.close()
