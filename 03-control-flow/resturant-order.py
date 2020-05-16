#########
# author: moemen.ahmed@gmail.com
# date: 14 May 20
# purpose: show the different decision and control of the program flow in python
#########

### This program simulate a restaurant cashier order

menu = {1: ("rice",3500), 2: ("pasta",4500), 3: ("steak",11000), 4: ("fired chicken",9550), 5: ("green salad",5000), 6: ("lemon juice",2575), 7: ("water bottle",1500)}

# Display the menu
print("Welcome to the menu!")
for item in menu:
    print(f"{item} - {menu[item][0].ljust(15)}    Price: {float(menu[item][1] / 100)}")

# create a dictionary to receive the choice
order = {}

# ask for choices
o = int(input("Enter your choice, or press enter to proceed. "))
while (o != ""):
    o = int(o)
    if o in order:
        order[o] += 1
    elif o not in menu.keys():
        print("Invalid Option! Please enter an item number from the menu.")
        o = input("Enter your choice, or press enter to proceed. ")
        continue
    else:
        order[o] = 1
    o = input("Enter your choice, or press enter to proceed. ")

# show the order, calculate the toal and show on the screen
total = 0
print("You have ordered:")
for o in order:
    itemPrice = menu[o][1] * order[o]
    print(f"{order[o]} x {menu[o][0].ljust(15)}  = {float(itemPrice / 100)}")
    total += itemPrice    

print(f"\nThe total price is  {float(total / 100)}")
print("Thank you :-)")

