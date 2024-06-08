#define the menu of restaurant
menu = {
    'Pizza': 90,
    'Pasta': 50,
    'Burger': 60,
    'Coffee': 50,
    'Water': 20,
}

#Greet
print("Welcome to ZS Restaurant")
print(" Pizza: Rs 90\n Pasta: Rs 50\n Burger: Rs 60\n Coffee: Rs 50\n Water: Rs 20")

order_total = 0
#90 + 20 = 110

item_1 = input(" Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 90
    print(f" Your item {item_1} has been added to your order")
    
else:
    print(f" Ordered item{item_1} is not available yet!")
    
another_order = input(" Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2] #order_total + item_2
    print(f" Your item {item_2} has been added to your order")
    
else:
    print(f" Ordered item {item_2} is not available yet!")
    
print("The total amount of items to pay is {order_total}")


   