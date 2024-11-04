class ShoppingCart:
    listItems = []
    _total  = None
    def __init__(self, *items):
        #*items to pass many number of items when number of arguments is unknown
        self.listItems = list(items)
        #list(items) b/c *items is return as tuple of items

    def _calculateTotal(self):
        self._total = len(self.listItems)
        return self._total
    def add_Items(self , abc ):
        self.listItems.append(abc)
        return self.listItems
    def remove_items(self , xyz):
        if(xyz in self.listItems):
            self.listItems.remove(xyz)
            return self.listItems
        else: print("item no found in list")
        
    def getter(self):
        print(f"The Total items in cart Are : {self._calculateTotal()}")



cart =  ShoppingCart("fruits" , "veges" , "meat", "fish", "cold drinks")
print(cart.add_Items("chips"))
cart.getter()
cart.remove_items("mango")
print(cart.remove_items("fish"))
cart.getter()
# print("the total items in cart are" ,cart._calculateTotal())
#not a good approach for accessing protected attributes outside teh class


