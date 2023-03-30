from Database import Database
from Game import Game
import os
import re
class main:

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
                #validar que el modelo sea de 6 letras y 2 numeros
                game_id = input("Ingrese el modelo del juego: ")

                while (re.match(r"^[A-Z]{6}[0-9]{2}$", game_id) == None):
                    print("El modelo no es válido, por favor ingrese 6 letras y 2 numeros")
                    game_id = input("Ingrese el modelo del juego: ")

                #validar que el titulo sea de maximo 10 caracteres
                game_title = input("Ingrese el título del juego: ")

                while (len(game_title) > 10):
                    print("El título no es válido, por favor ingrese un título de máximo 10 caracteres")
                    game_title = input("Ingrese el título del juego: ")

                #validar que el precio sea un numero de maximo 3 digitos
                game_price = input("Ingrese el precio del juego: ")

                while (not game_price.isnumeric()) or (int(game_price) > 999):
                    print("El precio no es válido, por favor ingrese un número de máximo 3 dígitos")
                    game_price = input("Ingrese el precio del juego: ")

                game_price = int(game_price)
                new_game = Game(game_id, game_title, game_price)
                
                database.add_game(new_game)

            elif option == "2":
                game_title = input("Ingrese el título del juego: ")
                database.delete_game_by_title(game_title)

            elif option == "3":
                game_title = input("Ingrese el título del juego: ")
                if database.get_game_id_by_title(game_title) == None:
                    print("No se encontró el juego")
                else:
                    database.rent_game(database.get_game_id_by_title(game_title))
                    print("El juego se ha alquilado exitosamente")
            
            elif option == "4":
                game_title = input("Ingrese el título del juego: ")
                if database.get_game_id_by_title(game_title) == None:
                    print("No se encontró el juego")
                else:
                    database.return_game(database.get_game_id_by_title(game_title))
                    print("El juego se ha devuelto exitosamente")
            
            elif option == "5":
                game_id = input("Ingrese el modelo del juego: ")
                game = database.get_game_by_id(game_id)
                if game != None:
                    game.print_attributes()
                else:
                    print("No se encontró el juego")
            
            elif option == "6":
                game_title = input("Ingrese el título del juego: ")
                game = database.get_game_by_title(game_title)
                if game == None:
                    print("No se encontró el juego")
                else:
                    game.print_attributes()

            elif option == "7":
                database.erase_db()
            
            else:
                database.save_db_json()
                print("Gracias por usar Rent-A-Game Caracas. Vuelva pronto")
                keepGoing = False
        
            

main = main()
main.run()   
