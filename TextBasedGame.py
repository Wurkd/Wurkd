# Project 2 Temisanren Odumu IT-140

print("Welcome to Luigi's Mansion 👻")
print()
print("Collect all the items in order to release mario from King Boo's Painting")
print()
print("To move throughout the mansion to each room type your direction: North, South, East, West")
print()
print("Type the name of the item in the room to add to your inventory")
print()

rooms = {
    'Grand Living Room':{ 'South':'Foyer', 'North':'Sun Room', 'East':'Library', 'West':'Master Bedroom' },
    'Foyer':{ 'North':'Grand Living Room', 'East':'Bed Room 1'},
    'Bed Room 1':{ 'West':'Foyer'},
    'Library':{ 'West':'Grand Living Room', 'North':'Guest Room'},
    'Guest Room':{ 'South':'Library'},
    'Sun Room':{ 'South':'Grand Living Room', 'East':'Pool House', 'item':'Mario\'s Star' },
    'Pool House':{ 'West':'Sun Room' },
    'Master Bedroom':{ 'East':'Grand Living Room' }
}
items = {
    'Foyer':'Mario\'s Shoes',
    'Bed Room 1':'Mario\'s Gloves',
    'Grand Living Room':'Polturgust 3000',
    'Library':'Key to Master',
    'Guest Room':'Mario\'s Hat',
    'Sun Room':'Mario\'s Star',
    'Master Bedroom':'KING BOO'
}

directions = ['North','South','East','West']
state = 'Foyer'
inventory = []

def get_new_state(state, direction):
    new_state = state  # declaring
    for i in rooms:  # loop
        if i == state:  # if
            if direction in rooms[i]:  # if
                new_state = rooms[i][direction]  # assigning new_state
    return new_state  # return


while 1:  # gameplay loop
    print('You are in the ', state)  # printing state
    if state == 'Master Bedroom':
        print('Battling with KING BOO', end='')
        for i in range(50):
            for j in range(1000000):
                pass
            print(".", end='', flush=True)
        print()
        if len(inventory) == 6:
            print('You won - letsaaa goooooo')
        else:
            print('Sorry, you lost - be better armed next time')
        break

    print('Available to you in this room: ', items[state])
    print('You currently have', inventory)
    direction = input('Enter item you want OR direction to go OR exit to give up: ')  # asking user
    if direction.lower() == items[state].lower():
        if items[state] not in inventory:
            inventory.append(items[state])
            items[state] = 'No Items Available'
        continue

    direction = direction.capitalize()  # making first character capital remaining lower
    if direction == 'Exit':  # if
        exit(0)  # exit function
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':  # if
        new_state = get_new_state(state, direction)  # calling function
        if new_state == state:  # if
            print('You have ran into a ghastly wall. Try another direction!!')  # print ## tell user what is happening
        else:
            state = new_state  # changing state value to new_state
    else:
        print('Invalid command!!')  # print ## possibly make this more generic