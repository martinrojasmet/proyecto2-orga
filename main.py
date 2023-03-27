class main:

    def __init__(self):
        self._init()

    def validate_game_att(self, id, title, price):
        if id == "" or title == "" or price == "":
            return False
        else:
            return True