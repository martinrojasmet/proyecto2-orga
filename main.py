import re

class main:

    def validate_game_att(self, game):
        valid_game = True
        if not re.match(r"^[a-zA-Z]{4}[0-9]{2}$", game.get_id()):
            valid_game = False
        if  game.get_title().len() > 10:
            valid_game = False
        if (game.get_price() > 999) and (not game.get_price().isnumeric()):
            valid_game = False
        return valid_game

main()