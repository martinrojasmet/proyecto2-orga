list=[
        [
            "Diablo",
            "DIABLO89"
        ],
        [
            "Domino",
            "DOMINO34"
        ],
        [
            "Doom",
            "DOOMMM64"
        ],
        [
            "DragnQuest",
            "DRAGON45"
        ],
        [
            "Fifa",
            "FIFAAA12"
        ],
        [
            "Magic",
            "MAGICC12"
        ],
        [
            "Mario Kart",
            "MARIOK45"
        ],
        [
            "MarioBros",
            "MARIOB67"
        ],
        [
            "Solitario",
            "SOLITA40"
        ],
        [
            "Sonic",
            "SONICC02"
        ],
        [
            "Spaceinv",
            "SPACEI27"
        ],
        [
            "Titans",
            "TITANS56"
        ],
        [
            "YugiOh",
            "YUGIOH66"
        ],
        [
            "frogger",
            "FROGGR33"
        ],
        [
            "TurboRace",
            "TURBOS65"
        ]]

def sort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i][0] > list[j][0]:
                list[i],list[j] = list[j],list[i]
    return list
list = sort(list)

list2 = []

#iterate and compare the first element of each list in list2
for i in range(len(list2)):
    for j in range(i+1,len(list2)):
        print(list2[i][0] < list2[j][0])

list2 = [
        [
            "Diablo",
            "DIABLO89"
        ],
        [
            "Domino",
            "DOMINO34"
        ],
        [
            "Doom",
            "DOOMMM64"
        ],
        [
            "DragnQuest",
            "DRAGON45"
        ],
        [
            "Fifa",
            "FIFAAA12"
        ],
        [
            "Magic",
            "MAGICC12"
        ],
        [
            "Mario Kart",
            "MARIOK45"
        ],
        [
            "MarioBros",
            "MARIOB67"
        ],
        [
            "Meteor",
            "METEOR60"
        ],
        [
            "Solitario",
            "SOLITA40"
        ],
        [
            "Sonic",
            "SONICC02"
        ],
        [
            "Spaceinv",
            "SPACEI27"
        ],
        [
            "Titans",
            "TITANS56"
        ],
        [
            "TurboRace",
            "TURBOS65"
        ],
        [
            "YugiOh",
            "YUGIOH66"
        ],
        [
            "frogger",
            "FROGGR33"
        ]
    ]


for i in range(len(list2)):
    for j in range(i+1,len(list2)):
        print(list2[i][0] < list2[j][0])