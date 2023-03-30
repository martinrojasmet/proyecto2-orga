list=[
        [
            "frogger",
            "FROGGR33"
        ],
        [
            "Spaceinv",
            "SPACEI27"
        ],
        [
            "MarioBros",
            "MARIOB67"
        ],
        [
            "Mario Kart",
            "MARIOK45"
        ],
        [
            "YugiOh",
            "YUGIOH66"
        ],
        [
            "Magic",
            "MAGICC12"
        ],
        [
            "Sonic",
            "SONICC02"
        ],
        [
            "Titans",
            "TITANS56"
        ],
        [
            "Domino",
            "DOMINO34"
        ],
        [
            "Solitario",
            "SOLITA40"
        ],
        [
            "Doom",
            "DOOMMM64"
        ],
        [
            "Diablo",
            "DIABLO89"
        ],
        [
            "DragnQuest",
            "DRAGON45"
        ],
        [
            "Fifa",
            "FIFAAA12"
        ]]

def sort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i][0] > list[j][0]:
                list[i],list[j] = list[j],list[i]
    return list
list = sort(list)
print(list)