my_dict = {}

repeat = True
while repeat:
    name = input("What is your name?:\n")
    bid = int(input('Whats your bid?:\n'))
    next = input('Are there any other bidders? Type "yes" to continue, or "no" to end auction.').lower()
    my_dict[name] = bid
    if next == "no":
        print('thanks for participating in the auction')
        
        winner_value = max(my_dict.values())
    
        for key,values in my_dict.items():
            if winner_value == values:
                print(f'the auction winner is {key} with {winner_value}$ of bid ammount')
                break
        repeat = False
    else:
        print("\n" * 90)

#leap year finder:

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else: 
#                 return False
#         else:
#             return True
#     else:
#         return False
        
# print(is_leap_year(1700))
#     # Write your code here. 
#     # Don't change the function name.