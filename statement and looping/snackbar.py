'''3.Write an app to calculate the total bill at the Snack bar. The price of coffee is Rs 100, Vadai (1) is Rs100,
   Sandwich is Rs 200, Coke Rs 60. If the customer buys more than one sandwich or two or more vadai, 
   the price of one coffee  is Rs 50. 
   If the customer buys one of each item, then there is discount of 20% of the total. No further discounts after the 20% discount.
   If the total price of the bill (before any discount) is more than Rs1000, then also there is a 20% discount. 
'''
price_of_coffee = 100
price_of_sandwich = 200
price_of_vadai = 100
price_of_coke=60
discount_offer = 0.2
discount_amount = 0

no_of_vadai=int(input("Enter the number of vadai you bought: "))
no_of_coffee=int(input("Enter How Many coffee you bought: "))
no_of_sandwich=int(input("Enter the number of sandwich you bought: "))
no_of_coke=int(input("Enter How Many coke You bought:"))

if no_of_vadai >= 1 and no_of_coffee >= 1 and no_of_sandwich >= 1 and     no_of_coke>=1:
    if no_of_sandwich > 1 or no_of_vadai >=2 :
        price_of_coffee = 50
        total_amount = (no_of_coffee * price_of_coffee) + (no_of_sandwich * price_of_sandwich) + (no_of_vadai * price_of_vadai)+(no_of_coke*price_of_coke)
    else:
        total_amount = (no_of_coffee * price_of_coffee) + (no_of_sandwich * price_of_sandwich) + (no_of_vadai * price_of_vadai)+(no_of_coke*price_of_coke)
        discount_amount = total_amount * discount_offer 
        total_amount = total_amount - discount_amount
else:
    total_amount = (no_of_coffee * price_of_coffee) + (no_of_sandwich * price_of_sandwich) + (no_of_vadai * price_of_vadai)+(no_of_coke*price_of_coke)


if total_amount > 1000 and discount_amount == 0 and price_of_coffee == 100:
    discount_amount = total_amount * discount_offer 
    total_amount = total_amount - discount_amount
    print(f"Your total bill amount: {total_amount}")
else:
    print(f"Your total bill amount: {total_amount}")
