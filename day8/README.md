u can use dictionary to store functions also if u have multiple functions in the code u can store them as values with you own keys and if there is need of selecting one random function from the functions u can easliy use the dict[key](function value pairs ).

for example:

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

operations = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div,
            "%": mod
        }
        answer = operations[operation](n1, n2)

here operation is the the operator selected by user and 
n1 and n2 are the values selected by user.
