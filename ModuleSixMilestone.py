# Temisan Odumu IT 140
enter = int(input('Press 1 to enter through the Great hall:'))

rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
        }
directions = ['North','South','East','West']
startingroom = rooms['Great Hall']

while True:
    # display current location
    print()
    # get user input
    command = input('\nMove North South East or West or quit').strip()
    # movement
    if command in directions:
        if command in startingroom:
            startingroom = rooms[startingroom[command]]
        else:
            # bad movement
            print("You can't go that way.")
    # quit game
    elif command.lower() in ('q', 'quit'):
        break
    # bad command
    else:
        print("I don't understand that command.")

