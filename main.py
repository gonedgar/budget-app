from budget import Category

clothing = Category('Clothing')
clothing.deposit(17.50, "First clothing deposit")
clothing.withdraw(10.25, 'Bought a shirt')
print(clothing.category+" balance:",clothing.get_balance())

food = Category('food')
food.deposit(1, 'First food deposit')
clothing.transfer(25, food)
print(clothing.category+':', clothing.ledger)
print(food.category+" balance:",food.get_balance())
print(food.category+':',food.ledger)
