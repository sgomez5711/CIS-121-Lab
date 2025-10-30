
class Product:

    # This will run first as we create the class
    def __init__(self, input_name, input_price):
        # private class variables
        self.name = input_name
        self.price = input_price
        self.quantity = 0
    
    #Set method
    def set_quantity(self, value):
        if 0 <= value <99:
            self.quantity = value
        
    # Build in print method
    def __str__(self):
        return f"The product is {self.name} and priced at {self.price} we have {self.quantity}"
    
apple_iphone = Product("Iphone 17 Pro Max", 1499)
apple_watch = Product("Apple Watch Series 7", 499)

print(apple_iphone)
print(apple_watch)

apple_watch.set_quantity(5)

print(apple_watch)
