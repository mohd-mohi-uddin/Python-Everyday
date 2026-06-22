import string

logo = '''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           

'''
print(logo)

#ENCRYTION:

def encryption(message,shift):
    alphabet = string.ascii_lowercase
    
    encrypted_message = ""

    for i in message:
        if i not in alphabet:
            encrypted_message += i
            
        else:
            position = alphabet.index(i)
            new_index = position + shift
            if new_index > 25:
                new_index %= 26
        
            encrypted_message += alphabet[new_index] 
    return encrypted_message


def decryption(message,shift):
    alphabet = string.ascii_lowercase
    
    decrypted_message = ""

    for i in message:
        if i == " ":
            decrypted_message += i
        else:
            position = alphabet.index(i)
            new_index = position - shift
            if new_index > 25:
                new_index %= 26
        
            decrypted_message += alphabet[new_index] 
    return decrypted_message



gameover = False
while not gameover:
    user_need = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if user_need == "encode":
        user_message = input("\nType your message:\n").lower()
        user_shift = int(input("\nType the shift number:\n").lower())
        print(f"\nHere is the {user_need} result: {encryption(user_message,user_shift)}")


    elif user_need == "decode":
        user_message = input("\nType your message:\n").lower()
        user_shift = int(input("\nType the shift number:\n").lower())
        print(f"\nHere is the {user_need} result: {decryption(user_message,user_shift)}")

    else:
        print("You have typed the wrong spelling, please type again.")

    second_need = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()

    if second_need == "no":
        gameover = True
        print("Goodbye")

    
        
    
        

    

    