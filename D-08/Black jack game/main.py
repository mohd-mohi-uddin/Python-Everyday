import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = random.sample(cards,2)
dealer_cards = random.sample(cards,2)

if len(user_cards) == 2 and sum(user_cards) == 21:
    print(f"BLACKJACK, YOU WON!")

elif len(dealer_cards) ==2 and sum(dealer_cards) == 21:
    print("Dealer got BLACKJACK! , YOU LOSE")

else:
    if sum(user_cards) == 22:
        total = sum(user_cards) - 10
    else:
        total = sum(user_cards)

    if sum(dealer_cards) == 22:
        dealer_total = sum(dealer_cards) - 10
    else:
        dealer_total = sum(dealer_cards)
    
    print(f"your cards are: {user_cards} and your total is {total} ")

    dealer_known_card = dealer_cards[0]
    print(f"dealer one card is: [{dealer_known_card},_]")

    def draw_card():
        total = sum(user_cards)
        ace = random.choice(cards)
        if ace == 11:
            new_total = total + 11
            if new_total > 21:
                user_cards.append(1)
            else:
                user_cards.append(11)
        else:
            user_cards.append(ace)
        total = sum(user_cards)
        print(f"\n\nyour cards are {user_cards} and your total is {total}")

    def result():
        if total > dealer_total:
            print(f"you won, your total is {total} and dealer's total is {dealer_total} and cards were {dealer_cards}")
        elif total < dealer_total:
            if dealer_total > 21:
                print(f"you won, your total is {total} and dealer's total is {dealer_total} and cards were {dealer_cards}")
            else:
                print(f"your cards are {user_cards} and dealer cards are {dealer_cards}.\nyou lose, your total is {total} and dealer's total is {dealer_total}")
        elif total == dealer_total:
            print("DRAW")

    gameover = True

    while gameover:

        step2 = input("press 'y' to draw one more card, or press 'n' to show your cards:\n").lower()
        
        if step2 == "y":
            draw_card()
            total = sum(user_cards)

            if total > 21:
                if 11 in user_cards:
                    total = total - 10
                    user_cards[user_cards.index(11)] = 1
                    print(f"your cards are now {user_cards} and your total is {total}")
                else:
                    print("you lose, the dealer wins")
                    gameover = False

        elif step2 == "n":
        
            while dealer_total < 17:
                dealer_cards.append(random.choice(cards))
                dealer_total = sum(dealer_cards)
                    
                if dealer_total > 21:
                    if 11 in dealer_cards:
                        dealer_cards.remove(11)
                        dealer_cards.append(1)
                        dealer_total = sum(dealer_cards)
                                
            result()
            gameover = False
               
                
        
                
            


    
