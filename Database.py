class Database:

    def __init__(self):

        self.matrix = [[],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       []]
        self.index_table = []

    def add_game(self, game):


            
            self.matrix[0].append(game.id)
            self.index_table.append(game.id)

    def hash_function(self, string):
        key = 0
        for c in string:
            key += ord(c)
        key = key % 3

        return key