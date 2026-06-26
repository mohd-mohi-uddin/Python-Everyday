import higher_lower_data
import random
LOGO = """"
 __   __  ___   _______  __   __  _______  ______   
|  | |  ||   | |       ||  | |  ||       ||    _ |  
|  |_|  ||   | |    ___||  |_|  ||    ___||   | ||  
|       ||   | |   | __ |       ||   |___ |   |_||_ 
|       ||   | |   ||  ||       ||    ___||    __  |
|   _   ||   | |   |_| ||   _   ||   |___ |   |  | |
|__| |__||___| |_______||__| |__||_______||___|  |_|
 ___      _______  _     _  _______  ______         
|   |    |       || | _ | ||       ||    _ |        
|   |    |   _   || || || ||    ___||   | ||        
|   |    |  | |  ||       ||   |___ |   |_||_       
|   |___ |  |_|  ||       ||    ___||    __  |      
|       ||       ||   _   ||   |___ |   |  | |      
|_______||_______||__| |__||_______||___|  |_|      
"""
print(LOGO)

logo2 = """"
##     ##  ######  
##     ## ##    ## 
##     ## ##       
##     ##  ######  
 ##   ##        ## 
  ## ##   ##    ## 
   ###     ######  
"""
data_list = higher_lower_data.data

option1 = random.choice(data_list)
option2 = random.choice(data_list)
score = 0

def options(want_score=True):
    global option1, score, option2
    option1 = option2
    option2 = random.choice(data_list)
    if want_score:
        score += 1
    return "\n" *100

while True:
    if score > 0:
        print(f"You are right!, your current score is :{score}")

    print(f"Compare A: {option1["name"]}, a {option1["description"]}, from {option1["country"]}")
    print(logo2)
    print(f"Compare B: {option2["name"]}, a {option2["description"]}, from {option2["country"]}")

    user_choice = input("Who has more followers? Type 'A' or 'B':\n").lower()
 
    if user_choice == "a":
        if option1["follower_count"] > option2["follower_count"]:
            print(options())
        elif option1["follower_count"] == option2["follower_count"]:
            print(options(False))
        elif option1["follower_count"] < option2["follower_count"]:
            print("wrong answer, game over.")
            break
    elif user_choice == "b":
        if option2["follower_count"] > option1["follower_count"]:
            print(options())
        elif option1["follower_count"] == option2["follower_count"]:
            print(options(False))
        elif option2["follower_count"] < option1["follower_count"]:
            print("wrong answer, game over.")
            break 
