import random


print(""" __    __ _ _                                                               _       _                                      _           _                            _       _                          
/ / /\ \ (_) |_ __ _ _ __ ___  _   _  __      __  ___ _   _ _ __ ___  _   _| | __ _| |_ ___  _ __ _______   _ __ _____   _| |_ _   _  | | _____  ___  ___ _ __ ___ (_)   __| | ___     __ _ _ __ _   _ 
\ \/  \/ / | __/ _` | '_ ` _ \| | | | \ \ /\ / / / __| | | | '_ ` _ \| | | | |/ _` | __/ _ \| '__|_  / _ \ | '__|_  / | | | __| | | | | |/ / _ \/ __|/ __| '_ ` _ \| |  / _` |/ _ \   / _` | '__| | | |
 \  /\  /| | || (_| | | | | | | |_| |  \ V  V /  \__ \ |_| | | | | | | |_| | | (_| | || (_) | |   / /  __/ | |   / /| |_| | |_| |_| | |   < (_) \__ \ (__| | | | | | | | (_| | (_) | | (_| | |  | |_| |
  \/  \/ |_|\__\__,_|_| |_| |_|\__, |   \_/\_/   |___/\__, |_| |_| |_|\__,_|_|\__,_|\__\___/|_|  /___\___| |_|  /___|\__,_|\__|\__,_| |_|\_\___/|___/\___|_| |_| |_|_|  \__,_|\___/   \__, |_|   \__, |
                               |___/                  |___/                                                                                                                           |___/      |___/ """)
print("""         _______      
        /\       \       
       /()\   ()  \      
      /    \_______\      
      \    /()     /       
       \()/   ()  /        
        \/_____()/
        
        """)


def rzut_koscia(rzut):

    if rzut == 1:
        print("""              ----- 
              |   |
              | o |
              |   |
              -----""")

    elif rzut == 2:
        print("""              -----
              |o  |
              |   |
              |  o|
              -----""")

    elif rzut == 3:
        print("""              -----
              |o  |
              | o |
              |  o|
              -----""")

    elif rzut == 4:
        print("""              -----
              |o o|
              |   |
              |o o|
              -----""")

    elif rzut == 5:
        print("""              -----
              |o o|
              | o |
              |o o|
              -----""")

    elif rzut == 6:
        print("""              -----
              |o o|
              |o o|
              |o o|
              -----""")


if __name__ == '__main__':
    ilosc_kostek = input('Iloma koscmi chesz rzucic :')
    suma = []

    try:
        if int(ilosc_kostek) == 1:
            rzut = random.randint(1, 6)
            rzut_koscia(rzut)
            print('')
            print(f"""
            
            Twoj wynik to : {rzut}""")

        elif int(ilosc_kostek) > 1:
            for x in range(0, int(ilosc_kostek)):
                rzut = random.randint(1, 6)
                suma.append(rzut)
                rzut_koscia(rzut)
                wynik_koncowy: int = sum(suma)
            print(f"""
            
            Twoj wynik to:{wynik_koncowy}""")

    except TypeError:
        print('By rzucic koscmi wprowadz dodatnia liczbe calkowita!')
    except ValueError:
        print('By rzucic koscmi wprowadz dodatnia liczbe calkowita!')











