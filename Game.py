class Game:

    def __init__(self, id, title, price, available = True):
        self.id = id
        self.title = title
        self.price = price
        self.available = available

    def set_available(self):
        self.available = True

    def set_not_available(self):
        self.available = False

    def change_price(self, price):
        self.price = price

    def print_availability(self):
        if self.available:
            print("En stock")
        else:
            print("Alquilado")
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "available": self.available
        }
    
    def print_attributes(self):
        print("")
        print("Atributos del juego: ")
        print("Modelo: ", self.id)
        print("Título: ", self.title)
        print("Precio: ", self.price)
        self.print_availability()
        print("")