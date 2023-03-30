class Game:

    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price
        self.available = True

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
    
    def print_attributes(self):
        print("Atributos del juego: ")
        print("Modelo: ", self.id)
        print("Título: ", self.title)
        print("Precio: ", self.price)
        self.print_availability()
        print("")