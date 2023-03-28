import numpy as np

class Database:

    def __init__(self):

        self.matrix = [[],
                       [],
                       [],
                       [], #overflow
                       [],
                       [],
                       [],
                       [],
                       []]
        self.index_table = []

    def add_game(self, game):

        address = hash_function(game.id)
        register_full = register_is_full(address)
        game_in_table = game_in_table(game.id, address)
        game_in_index_table = game_in_index_table(game.title)

        if not register_full:
            if not game_in:
                if not game_in_index_table:
                    self.matrix[address].append(game)
                    self.index_table.append([game.title, address])
                else:
                    print("El juego ya existe (titulo)")
            else:
                print("El juego ya existe (modelo)")
        else:
            new_address = check_empty_register()
            if new_address != 10:
                if not game_in:
                    if not game_in_index_table:
                        self.matrix[new_address].append(game)
                        self.index_table.append([game.title,new_address])
                    else:
                        print("El juego ya existe (titulo)")
                else:
                    print("El juego ya existe (modelo)")
            else:
                print("No hay espacio en la base de datos")

    def hash_function(self, string):
        key = 0
        for c in string:
            key += ord(c)
        key = key % 3
        return key

    def game_in_table(self, game_id, address):
        result = False
        for i in range(0,len(self.matrix[address])):
            if self.matrix[address][i].id == game_id:
                result = True
        return result

    def register_is_full(self, address):
        result = False
        if len(self.matrix[address]) == 3:
            result = True
        return result

    def game_in_index_table(self, game_title):
        result = False
        for i in range(0,len(self.index_table)):
            if self.index_table[i][0] == game_title:
                result = True
        return result

    def check_empty_register(self, address):
        result = 10
        for i in range(3,10):
            if len(self.matrix[i]) < 3:
                result = i
        return result

    def address_game_by_title(self, game_title):
        result = 10
        for i in range(0,len(self.index_table)):
            if self.index_table[i][0] == game_title:
                result = self.index_table[i][1]
        return result

    def get_game_by_title(self, game_title):
        address = self.address_game_by_title(game_title)
        result = None
        if address == 10:
            print("El juego no existe")
        else:
            for i in range(0,len(self.matrix[address])):
                if self.matrix[address][i].title == game_title:
                    result = self.matrix[address][i]
        return result

    def address_game_by_id(self, game_id):
        result = 10
        address = self.hash_function(game_id)
        for i in range(0,len(self.matrix[address])):
            if self.matrix[address][i].id == game_id:
                result = address
        return result

    def get_game_by_id(self, game_id):
        address = self.address_game_by_id(game_id)
        result = None
        if address == 10:
            print("El juego no existe")
        else:
            for i in range(0,len(self.matrix[address])):
                if self.matrix[address][i].id == game_id:
                    result = self.matrix[address][i]
        return result

    def return_game(self, game_id):
        game = self.get_game_by_id(game_id)
        if game != None:
            game.set_available()
        else:
            print("El juego no existe")

    def rent_game(self, game_id):
        game = self.get_game_by_id(game_id)
        if game != None:
            game.set_not_available()
        else:
            print("El juego no existe")

    def delete_game(self, game_id):
        address = self.address_game_by_id(game_id)
        if address == 10:
            print("El juego no existe")
        else:
            for i in range(0,len(self.matrix[address])):
                if self.matrix[address][i].id == game_id:
                    self.matrix[address].pop(i)