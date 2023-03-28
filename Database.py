import numpy as np

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

    def get_matrix(self):
        return self.matrix

    def get_index_table(self):
        return self.index_table

    def add_game(self, game):

        address = hash_function(game.get_id())
        register_full = register_is_full(address)
        game_in_table = game_in_table(game.get_id(), address)
        game_in_index_table = game_in_index_table(game.get_title())

        if not register_full:
            if not game_in:
                if not game_in_index_table:
                    self.get_matrix[address].append(game)
                    self.get_index_table.append([game.get_title(), address])
                else:
                    print("El juego ya existe (titulo)")
            else:
                print("El juego ya existe (modelo)")
        else:
            new_address = check_empty_register()
            if new_address != 10:
                if not game_in:
                    if not game_in_index_table:
                        self.get_matrix()[new_address].append(game)
                        self.get_index_table().append([game.get_title(),new_address])
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
        for i in range(0,len(self.get_matrix()[address]))):
            if self.get_matrix()[address][i].get_id() == game_id:
                result = True
        return result

    def register_is_full(self, address):
        result = False
        if len(self.get_matrix()[address]) == 3:
            result = True
        return result

    def game_in_index_table(self, game_title):
        result = False
        for i in range(0,len(self.get_index_table())):
            if self.get_index_table()[i][0] == game_title:
                result = True
        return result

    def check_empty_register(self, address):
        result = 10
        for i in range(3,10):
            if len(self.get_matrix()[i]) < 3:
                result = i
        return result

    def address_game_by_title(self, game_title):
        result = 10
        for i in range(0,len(self.get_index_table())):
            if self.get_index_table()[i][0] == game_title:
                result = self.get_index_table()[i][1]
        return result

    def get_game_by_title(self, game_title):
        address = self.address_game_by_title(game_title)
        result = None
        if address == 10:
            print("El juego no existe")
        else:
            for i in range(0,len(self.get_matrix()[address])):
                if self.get_matrix()[address][i].get_title() == game_title:
                    result = self.get_matrix()[address][i]
        return result

    def address_game_by_id(self, game_id):
        result = 10
        address = self.hash_function(game_id)
        for i in range(0,len(self.get_matrix()[address])):
            if self.get_matrix()[address][i].get_id() == game_id:
                result = address
        return result

    def get_game_by_id(self, game_id):
        address = self.address_game_by_id(game_id)
        result = None
        if address == 10:
            print("El juego no existe")
        else:
            for i in range(0,len(self.get_matrix()[address])):
                if self.get_matrix()[address][i].get_id() == game_id:
                    result = self.get_matrix()[address][i]
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
            for i in range(0,len(self.get_matrix()[address])):
                if self.get_matrix()[address][i].get_id() == game_id:
                    self.get_matrix()[address].pop(i)