class Game:

    def __init__(self, id, title, price)
    self.id = id
    self.title = title
    self.price = price
    self.available = True

    
    def availability(self):
        return self.available

    def title(self):
        return self.title

    def price(self):
        return self.price

    def set_is_available(self):
        self.availability() = True

    def set_is_not_available(self):
        self.availability() = False

    def change_price(self, price):
        self.price() = price