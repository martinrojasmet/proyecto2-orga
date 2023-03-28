class Game:

    def __init__(self, id, title, price)
        self.id = id
        self.title = title
        self.price = price
        self.available = True

    def get_id(self):
        return self.id
    
    def get_available(self):
        return self.available

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def set_available(self):
        self.get_available() = True

    def set_not_available(self):
        self.get_available() = False

    def change_price(self, price):
        self.get_price() = price

    def print_availability(self):
        if self.get_available():
            print("En stock")
        else:
            print("Alquilado")