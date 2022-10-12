
# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.
#
# food_menu = {
#     "Starter" : ["Salad","Soup","Lamb chops"],
#     "main meals" : ["chicken & rice","Curry", "Chicken creamy pasta"],
#     "Drinks" : ["fanta","coke","water"],
#     "Dessert" : ["Chocolate cake", "Strawberry cake"]
# }
#
# print(food_menu)

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten


new_order = []

list_length = 3

for idx in range(list_length):
    item = input('Enter item to order: ')
    new_order.append(item)

print(new_order)

# --------------------------

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

print(f'Your order is {new_order} is that correct')

user = input()

