from budget import Category
from budget import print_category

# print(clothing.category+" balance:",clothing.get_balance())

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print_category(food)
# print(clothing.category+':', clothing.ledger)
# print(food.category+" balance:",food.get_balance())
# print(food.category+':',food.ledger)