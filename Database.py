import json
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

        address = self.hash_function(game.id)
        group_full = self.group_is_full(address)
        game_in_group = self.game_in_group(game.id, address)
        game_in_index_table = self.game_in_index_table(game.title)

        if not group_full:
            if not game_in_group:
                if not game_in_index_table:
                    self.matrix[address].append(game)
                    self.index_table.append([game.title, game.id])
                else:
                    print("El juego ya existe (titulo)")
            else:
                print("El juego ya existe (modelo)")
        else:
            new_address = check_empty_register()
            if new_address != 10:
                if not game_in_group:
                    if not game_in_index_table:
                        self.matrix[new_address].append(game)
                        self.index_table.append([game.title, game.id])
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

    def first_table_full(self, address):
        result = False
        if len(self.matrix[address] == 3):
            result = True
        return result

    def game_is_in_table(self, game_id, address):
        result = False
        for i in range(0,len(self.matrix[address])):
            if self.matrix[address][i].id == game_id:
                result = True
        return result

    def game_in_group(self, game_id, address):
        result = False
        if (address == 1):
            result = self.game_is_in_table(game_id, address)
            if (not result):
                new_address = 3
                while (not result) and (address < 5):
                    result = self.game_is_in_table(game_id, new_address)
                    new_address += 1
         
        elif (address == 2):
            result = self.game_is_in_table(game_id, address)
            if (not result):
                new_address = 5
                while (not result) and (address < 7):
                    result = self.game_is_in_table(game_id, new_address)
                    new_address += 1
            
        else:
            result = self.game_is_in_table(game_id, address)
            if (not result):
                new_address = 7
                while (not result) and (address < 9):
                    result = self.game_is_in_table(game_id, new_address)
                    new_address += 1

        return result

    def group_is_full(self, address):
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

    def check_empty_register(self, original_address):
        result = 10

        if original_address == 0:
            for i in range(3,5):
                if len(self.matrix[i]) < 3:
                    result = i

        elif original_address == 1:
            for i in range(5,7):
                if len(self.matrix[i]) < 3:
                    result = i

        else:
            for i in range(7,9):
                if len(self.matrix[i]) < 3:
                    result = i

        return result

    def address_game_by_title(self, game_title):
        result = 10
        for i in range(0,len(self.index_table)):
            if self.index_table[i][0] == game_title:
                result = self.hash_function(self.index_table[i][1])
        return result

    def get_game_by_title(self, game_title):
        address = self.address_game_by_title(game_title)
        result = None
        if address == 10:
            print("El juego no existe")
        else:
            if not self.group_is_full(address):
                for i in range(0,len(self.matrix[address])):
                    if self.matrix[address][i].title == game_title:
                        result = self.matrix[address][i]
            else:
                for i in range(0,len(self.matrix[address])):
                    if self.matrix[address][i].title == game_title:
                        result = self.matrix[address][i]
                if result == None:
                    if address == 0:
                        for i in range(3,5):
                            for j in range(0,len(self.matrix[i])):
                                if self.matrix[i][j].title == game_title:
                                    result = self.matrix[i][j]
                    elif address == 1:
                        for i in range(5,7):
                            for j in range(0,len(self.matrix[i])):
                                if self.matrix[i][j].title == game_title:
                                    result = self.matrix[i][j]
                    else:
                        for i in range(7,9):
                            for j in range(0,len(self.matrix[i])):
                                if self.matrix[i][j].title == game_title:
                                    result = self.matrix[i][j]    
        return result

    def get_game_by_id(self, game_id):
        address = self.hash_function(game_id)
        result = None
        game_is_in = self.game_in_group(game_id, address)

        if game_is_in:
            if not self.group_is_full(address):
                for i in range(0,len(self.matrix[address])):
                    if self.matrix[address][i].id == game_id:
                        result = self.matrix[address][i]
            else:
                for i in range(0,len(self.matrix[address])):
                    if self.matrix[address][i].id == game_id:
                        result = self.matrix[address][i]
                if result == None:
                    if address == 0:
                        for i in range(3,5):
                            for j in range(0,len(self.matrix[i])):
                                if self.matrix[i][j].id == game_id:
                                    result = self.matrix[i][j]
                    elif address == 1:
                        for i in range(5,7):
                            for j in range(0,len(self.matrix[i])):
                                if self.matrix[i][j].id == game_id:
                                    result = self.matrix[i][j]
                    else:
                        for i in range(7,9):
                            for j in range(0,len(self.matrix[i])):
                                if self.matrix[i][j].id == game_id:
                                    result = self.matrix[i][j]
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

    def delete_game_by_id(self, game_id):
        address = self.hash_function(game_id)
        game_is_in = self.game_in_group(game_id, address)
        if game_is_in:

            for i in range(0,len(self.index_table)):
                if self.index_table[i][1] == game_id:
                    self.index_table.pop(i)

            if self.game_is_in_table(game_id, address):
                for i in range(0,len(self.matrix[address])):
                    if self.matrix[address][i].id == game_id:
                        self.matrix[address].pop(i)
            else:
                if address == 0:
                    for i in range(3,5):
                        for j in range(0,len(self.matrix[i])):
                            if self.matrix[i][j].id == game_id:
                                self.matrix[i].pop(j)

                elif address == 1:
                    for i in range(5,7):
                        for j in range(0,len(self.matrix[i])):
                            if self.matrix[i][j].id == game_id:
                                self.matrix[i].pop(j)

                else:
                    for i in range(7,9):
                        for j in range(0,len(self.matrix[i])):
                            if self.matrix[i][j].id == game_id:
                                self.matrix[i].pop(j)

        else:
            print("El juego no existe")

    def delete_game_by_title(self, game_title):
        found = False
        for i in range(0,len(self.index_table)):
            if self.index_table[i][0] == game_title:
                self.delete_game_by_id(self.index_table[i][1])
                found = True
        if not found:
            print("El juego no existe")

    def save_db_json(self):
        dict = {"matrix": self.matrix, "index_table": self.index_table}
        with open("db.json", "w") as file:
            json.dump(dict, file)

    def erase_db_json(self):
        dict = {}
        with open("db.json", "w") as file:
            json.dump(dict, file)

    def erase_db(self):
        self.matrix = [[],[],[],[],[],[],[],[],[]]
        self.index_table = []
        self.erase_db_json()

    def get_id_by_title():
        result = None
        found = False
        for i in range(0,len(self.index_table)):
            if self.index_table[i][0] == game_title:
                found = True
        if found:
            result = self.index_table[i][1]
        return result

    def load_db_json(self):
        with open("db.json", "r") as file:
            dict = json.load(file)
            self.matrix = dict["matrix"]
            self.index_table = dict["index_table"]