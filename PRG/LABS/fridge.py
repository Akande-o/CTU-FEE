class Product:
    def __init__(self, name, qty, unit):
        self.name = name
        self.qty = qty
        self.unit = unit
    def inc(self, by):
        self.qty += by
    def use (self, qty):
        if qty > self.qty:
            self.qty = 0
        else:
            self.qty -= qty
    def __str__(self):
        return "{} {} of {}".format(self.qty, self.unit, self.name)

class Fridge:
    def __init__(self):
        self.products = []
    def add(self, name, qty, unit):
        p = Product(name, qty, unit)
        self.products.append(p)
    def inc(self, name, by):
        for product in self.products:
            if product.name == name:
                product.inc(by)
                break
    def use(self, name, qty):
        for product in self.products:
            if product.name == name:
                product.use(qty)
                if product.qty == 0:
                    self.products.remove(product)
    def __str__(self):
        return_string = "Fridge:\n"
        for product in self.products:
            return_string += "...{}\n".format(product)
        return return_string
if __name__ == "__main__":
    product1 = Product("tomatoes", 10, "pieces")
    print(product1)
    product1.inc(2)
    print(product1)
    product1.use(5)
    print(product1)
    product1.use(10)
    print(product1)
    fridge = Fridge()
    fridge.add("tomatoes", 10, "pieces")
    fridge.add("onions", 3, "pieces")
    fridge.add("eggs", 12, "pieces")
    fridge.add("butter", 500, "grams")
    fridge.add("oil", 1, "liter")
 
    print(fridge)

    fridge.inc("onions", 8)
 
    print(fridge)

    fridge.use("butter", 200)
 
    print(fridge)
 
    fridge.use("butter", 500)
 
    print(fridge)
 
    