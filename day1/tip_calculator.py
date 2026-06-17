print("Welcome to the tip calculator!\n")
bill_total = float(input("What was the total bill? :"))
tip_perecent_cal = float(input("\nHow much tip would u like to give? [10, 12, 15]:"))
split =float(input("\nHow many people to split the bill? :"))
split_amount = (bill_total+bill_total*(tip_perecent_cal/100))/split
print(f"\nEach person should pay:{round(split_amount,2)}")


