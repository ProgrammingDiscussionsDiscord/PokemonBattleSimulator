"""
Program that generates pokemon
"""
import pandas as pd

pokemon = pd.read_csv('pokemon.csv')

natures = {
    "Adamant":
        {"increased": "Attack",
         "decreased": "Sp. Atk"},
    "Bashful":
        {"increased": None, 
         "decreased": None},
    "Bold":
        {"increased": "Defense",
         "decreased": "Attack"},
    "Brave":
        {"increased": "Attack", 
         "decreased": "Speed"},
    "Calm":
        {"increased": "Sp. Def",
         "decreased": "Attack"},
    "Careful":
        {"increased": "Sp. Def",
         "decreased": "Sp. Atk"},
    "Docile":
        {"increased": None,
         "decreased": None},
    "Gentle":
        {"increased": "Sp. Def",
         "decreased": "Defense"},
    "Hardy":
        {"increased": None,
         "decreased": None},
    "Hasty":
        {"increased": "Speed",
         "decreased": "Defense"},
    "Impish":
        {"increased": "Defense",
         "decreased": "Sp. Atk"},
    "Jolly":
        {"increased": "Speed",
         "decreased": "Sp. Atk"},
    "Lax":
        {"increased": "Defense",
         "decreased": "Sp. Def"},
    "Lonely":
        {"increased": "Attack",
         "decreased": "Defense"},
    "Mild":
        {"increased": "Sp. Atk",
         "decreased": "Defense"},
    "Modest":
        {"increased": "Sp. Atk",
         "decreased": "Attack"},
    "Naive":
        {"increased": "Speed",
         "decreased": "Sp. Def"},
    "Naughty":
        {"increased": "Attack",
         "decreased": "Speed"},
    "Quiet":
        {"increased": "Sp. Atk",
         "decreased": "Speed"},
    "Quirky":
        {"increased": None,
         "decreased": None},
    "Rash":
        {"increased": "Sp. Atk",
         "decreased": "Sp. Def"},
    "Relaxed":
        {"increased": "Defense", 
         "decreased": "Speed"},
    "Sassy":
        {"increased": "Sp. Def",
         "decreased": "Speed"},
    "Serious":
        {"increased": None,
         "decreased": None},
    "Timid":
        {"increased": "Speed",
         "decreased": "Attack"}
}

print("Welcome to the Pokémon JSON generator!  What pokemon would you",
      "like to create?\n")
found = False
while True:
    name = input().capitalize()
    choice = pokemon.loc[pokemon['Name'] == name][:]
    if name in pokemon.Name.values:
        break
    else:
        print("That name couldn't be found, try again!\n") 

print("You've chosen {}!  What level would you like {} to be?\n".format(choice.Name.values[0], choice.Name.values[0]))
while True:
    try:
        level = int(input())
    except ValueError:
        print("Not an integer! Try again, pick a number between 1 and 100\n")
        continue
    if level < 1 or level > 100:
        print("Choose a valid level between 1 and 100\n")
        continue
    break

retJSON = {}
retJSON['level'] = level
for field in choice:
    retJSON[field] = choice[field].values[0]

evRemaining = 510

stats = ['HP', 'Attack', 'Defense', 'Sp. Attack', 'Sp. Defense', 'Speed']
for key in stats:
    print('you have {} points remaining, you can put up to 255 points in a single stat.\nHow many points would you like to put into {}\n'.format(evRemaining, key))
    while True:
        if evRemaining == 0:
            print("Out of points!  Setting the rest to 0\n")
            ev_value = 0
            break
        try:
            ev_value = int(input())
        except ValueError:
            print("Not an integer! Try again, pick a number between 0 and 255\n")
            continue
        if ev_value < 0 or ev_value > 255:
            print("Choose a valid value between 0 and 255\n")
            continue
        if evRemaining - ev_value < 0:
            print("You don't have that many points left!  You have {} points\n".format(evRemaining))
            continue
        break
    retJSON['EV ' + key] = ev_value
    evRemaining -= ev_value

for key in stats:
    print("Pick a number 0 to 15 for {} IV (I'm not sure why you wouldn't pick 15)".format(key))
    while True:
        try:
            iv_value = int(input())
        except ValueError:
            print("Choose an integer between 0 and 15")
            continue
        if iv_value < 0 or iv_value > 15:
            print("Choose an integer between 0 and 15")
            continue
        retJSON['IV ' + key] = iv_value
        break
while True:
    print("Choose a nature\n")
    print(list(natures.keys()))
    nature = input()
    if nature in natures:
        retJSON['Nature'] = nature
        break

#  TODO given these stats, calculate the actual stats using that fancy equation


print(retJSON)
