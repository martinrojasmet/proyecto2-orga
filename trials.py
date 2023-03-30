from Database import Database
from Game import Game

class trials:

    def run(self):
        database = Database()

        game = Game("GTGTGT56", "Mario", 100)
        print(database.hash_function(game.id))

t = trials()
t.run()

#esto es para probar codigo aparte