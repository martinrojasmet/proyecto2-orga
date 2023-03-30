from Database import Database
from Game import Game

class trials:

    def run(self):
        database = Database()

        game = Game("MARIO1", "Mario", 100)
        print(database.check_empty_group(2))

t = trials()
t.run()

#esto es para probar codigo aparte