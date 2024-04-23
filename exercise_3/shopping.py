class Item:
    def __init__(self,preis,name):
        if(preis<0):
            raise ValueError("preis can not be lower than 0")
        self.preis=preis
        self.name=name
        
    def getPreis(self):
        return self.preis
    
    def getName(self):
        return self.name
        
class ShoppingCart:
    def __init__(self):
        self.items=[]
        
    # add item to cart
    def addItem(self,item):
        if(item.__class__.__name__!="Item"):
            raise TypeError("Given item has not the class 'Item'")
        self.items.append(item)
        
    # deletes item in cart with given index
    def deleteItem(self,index):
        if(index in range(0,len(self.items)-1)):
            del self.items[index]
        else:
            print("No item with given index")
            
    # returns false if cart is empty       
    def displayCart(self):
        items = self.items
        if (items==[]):
            print("Cart is empty")
            return False
        for item in items:
            print(f"{item.name} kostet {item.preis}")
            
    # returns number of items in cart
    def calculateQuantity(self):
        return len(self.items)