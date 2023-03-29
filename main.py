from Database import Database
from Game import Game
import os
import re
class main:

    def validate_game_att(self, game):
        valid_game = True
        if not (re.match(r"^[a-zA-Z]{4}[0-9]{2}$", game.id) != game.id):
            print("El id no es válido")
            valid_game = False
        if  len(game.title) > 10:
            print("El título no es válido")
            valid_game = False
        if (game.price > 999) and (not isinstance(game.price, int)):
            print("El precio no es válido")
            valid_game = False
        return valid_game

    def run(self):
        database = Database()
        keepGoing = True
        
        while (keepGoing):
            if os.stat("db.json").st_size != 0:
                database.load_db_json()

            print("""
            Bienvenido al sistema de alquiler de juegos Rent-A-Game Caracas

            1. Agregar juego
            2. Eliminar juego
            3. Alquilar juego
            4. Devolver juego
            5. Busqueda por modelo
            6. Busqueda por título
            7. Reiniciar los datos del programa
            8. Salir
            """)

            option = input("Ingrese el nro. de la opción que desee: ")

            if option == "1":
                game_id = input("Ingrese el id del juego: ")
                game_title = input("Ingrese el título del juego: ")
                game_price = input("Ingrese el precio del juego: ")
                game_price = int(game_price)
                new_game = Game(game_id, game_title, game_price)
                if self.validate_game_att(new_game):
                    database.add_game(new_game)

            elif option == "2":
                game_title = input("Ingrese el título del juego: ")
                database.delete_game_by_title(game_title)(game_title)

            elif option == "3":
                game_title = input("Ingrese el título del juego: ")
                database.rent_game(get_game_id_by_title(game_title))
            
            elif option == "4":
                game_title = input("Ingrese el título del juego: ")
                database.return_game(get_game_id_by_title(game_title))
            
            elif option == "5":
                game_id = input("Ingrese el id del juego: ")
                game = database.get_game_by_id(game_id)
                game.print_attributes()
            
            elif option == "6":
                game_title = input("Ingrese el título del juego: ")
                game = database.get_game_by_title(game_title)
                game.print_attributes()

            elif option == "7":
                database.erase_db()
            
            else:
                database.save_db_json()
                print("Gracias por usar Rent-A-Game Caracas. Vuelva pronto")
                keepGoing = False
            

main = main()
main.run()   
