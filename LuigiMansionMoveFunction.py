rooms = ['Foyer', 'Grand Living Room', 'Bed Room', 'Library', 'Master Bedroom', 'Guest Room', 'Sun Room', 'Pool House']
items = ['Poltergust 3000', 'Mario\'s Shoes', 'Mario\'s Gloves', 'Key to Master Bedroom', 'Mario\'s Hat', 'Mario\'s Star']


luigi = ''

def searchroom(x, y):
    print('You are in:',x, 'Press 1 to search this room')
    search = int(input())
    if search == 1:
        print('You received: ',y)


def move(direction, room, hero):
    if direction == 'North' and room == 'Foyer':
        hero = 'Luigi is in the Grand Living Room'
    if direction == 'East' and room == 'Foyer':
        hero = 'Luigi is in Bed Room 1'
    if direction == 'South' and room == 'Foyer':
        hero = 'Luigi can not move south'
    if direction == 'West' and room == 'Foyer':
        hero = 'Luigi can not move west'
    if direction == 'North' and room == 'Grand Living Room':
        hero = 'Luigi is in the Sun Room'
    if direction == 'East' and room == 'Grand Living Room':
        hero = 'Luigi is in the Library'
    if direction == 'South' and room == 'Grand Living Room':
        hero = 'Luigi is in the Foyer'
    if direction == 'West' and room == 'Grand Living Room':
        hero = 'Luigi can not move west without the Key'
    return hero





searchroom(rooms[0],items[1])
direction = input('Choose your direction: \'North\',\'South\',\'East\', or \'West\' ')
luigi = move(direction,rooms[0],luigi)
print(luigi)
if luigi == 'Luigi is in the Grand Living Room':
    searchroom(rooms[1], items[0])
    direction = input('Choose your direction: ')
    luigi = move(direction, rooms[1], luigi)
    print(luigi)







