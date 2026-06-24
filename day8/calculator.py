logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
  
def add(a1, b1):
    return a1 + b1

def sub(a2, b2):
    return a2 - b2

def mul(a3, b3):
    return a3 * b3

def div(a4, b4):
    return a4 / b4

def mod(a5, b5):
    return a5 % b5

# answer = ""
def calculator():
    n1 =float(input("What's the first number? :"))

    over = True
    while over:

        operation = input(f"+ \n- \n* \n/ \n% \nPick an operator:")
        n2 =float(input("What's the next number? :"))

    # if operation == "+":
    #     print(f"{n1}{operation}{n2} = {add(n1, n2)}")
    #     answer = add(n1, n2)

    # elif operation == "-":
    #     print(f"{n1}{operation}{n2} = {sub(n1, n2)}")
    #     answer = sub(n1, n2)

    # elif operation == "*":
    #     print(f"{n1}{operation}{n2} = {mul(n1, n2)}")
    #     answer = mul(n1, n2)

    # elif operation == "/":
    #     print(f"{n1}{operation}{n2} = {div(n1, n2)}")
    #     answer = div(n1, n2)

    # elif operation == "%":
    #     print(f"{n1}{operation}{n2} = {mod(n1, n2)}") 
    #     answer = mod(n1, n2)

    # else:
    #     print("Invalid Operator!, choose from the options")

                        #   ((((( OR )))))

        operations = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div,
            "%": mod
        }
        answer = operations[operation](n1, n2)
        print(f"{n1}{operation}{n2} = {answer}") 
        next_step = input(f"\nType 'y' to continue calculating with {answer} or type 'n' to start a new calculation:")
    
        if next_step == "y":
            n1 = answer
        #n1 = int(answer)
    # elif next_step == "n":
        # n1 = float(input("What's the first number? :"))
        else:
            over = False
            calculator()


calculator()

     