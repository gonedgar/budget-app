from budget import Category
from budget import print_category

clothing = Category('Clothing')
clothing.deposit(17.50, "First clothing deposit because I am not poor")
clothing.withdraw(10.25, 'Bought a shirt')
clothing.deposit(117.50, "First clothing deposit because I am not poor")
# print(clothing.category+" balance:",clothing.get_balance())

food = Category('Food')
food.deposit(1, 'First food deposit')
clothing.transfer(25, food)
# print(clothing.category+':', clothing.ledger)
# print(food.category+" balance:",food.get_balance())
# print(food.category+':',food.ledger)

print_category(clothing)
print_category(food)