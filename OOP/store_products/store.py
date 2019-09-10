import product

class Store:
    def __init__(self, name, product_list):
        self.name = name
        self.product_list = product_list
    def add_product(self, new_product):
        self.product_list.append(new_product.name)
        print(f"Product list: {self.product_list}")
        return self
    def sell_product(self, id):
        for id in self.product_list: 
            self.product_list.remove(id)
            return self
    def inflation(self, percent_increase):
        self.price += (self.price * percent_increase)
        return self  
    def set_clearance(self, category, percent_discount):
        self.price -= (self.price * percent_discount)
        return self         


Alberstons = Store("Alberstons", ["Lucky Charms", "Ground Turkey Meat", "Dish Soap"])

jimmies = Product("Franks", 10.00, "Meats")
cookies = Product("Oreos", 7.00, "Snacks")

Alberstons.add_product(cookies)
Alberstons.add_product(jimmies)
