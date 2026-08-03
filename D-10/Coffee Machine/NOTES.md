if a_followers > b_followers:
    return user_guess == "a"
else:
    return user_guess == "b"

here return user_guess == "a" means if the guess is a then only the the if is ture and the computer knows it so it returns true.
there is no need to tell computer to return true if guess == a

like wise in if statement:

if user_guess: is enough, no need to write if user_guess = True:

the comuter knows it.

>> TRY EXCEPT BLOCK:

if the user has entred a wrony input like instead of int they typed a string then we can again ask to input a int char.

in try we can give a try option

in the ecxcept option we can can again give him a chance.

try:
    input("")
except valueerror!:
    print("what to input)

    