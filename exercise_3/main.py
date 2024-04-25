from easy_shopping.calculator import Calculator
from easy_shopping.shopping import Item, ShoppingCart



# calculator = Calculator()
# print(calculator.add(7,5))
# print(calculator.subtract(34,21))
# print(calculator.multiply(54,2))
# print(calculator.divide(144,2))
# print(calculator.divide(45,0))


# create 3 items
item1=Item(20,"Tisch")
item2=Item(5,"Ball")
item3=Item(1000,"VR-Brille")

# crate cart and add 3 items
cart=ShoppingCart()
cart.addItem(item1)
cart.addItem(item2)
cart.addItem(item3)

# display cart with 3 items and calculate quantity
cart.displayCart()
cart.calculateQuantity()

#delete first item and recalculate
cart.deleteItem(0)
cart.calculateQuantity()
