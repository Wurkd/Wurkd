print('Hello Hero! Let\'s adventure and defeat the Villain')
print('Choose between an east wing door or west wing door to try and claim a weapon')
print('west wing doors can be opened by typing left')
print('east wing doors can be opened by typing right')
leftdoor = 'left'
rightdoor = 'right'
hero = 0

def getweaponleft(west):
    west = input()
    if west == leftdoor:
        print('received your weapon: wand')
    else:
        west = 'right'
    return west

def getweaponleft2(west):
    west = input()
    if west == leftdoor:
        print('received your weapon: sword')
    else:
        west = 'right'
    return west

def getweaponright(east):
    east = input()
    if east == rightdoor:
        print('received your weapon: shield')
    else:
        east = 'left'
    return east

while hero == 0:
    print('Let\'s move you to the first set of doors. Press 1')
    movenextdoor = int(input())
    hero += 25
    print('Choose a door to claim your first weapon')
    if getweaponleft(leftdoor) == 'right':
        print('Try again')
        hero = 0
    else:
        hero += 25
        if hero == 50:
            print('Let\'s move you to the second set of doors. Press 2')
            movenextdoor = int(input())
            print('Choose a door to claim your second weapon')
            if getweaponleft2(leftdoor) == 'right':
                print('Try again')
                hero = 0
            else:
                hero += 25
                if hero == 75:
                    print('Let\'s move you to the third set of doors. Press 3')
                    movenextdoor = int(input())
                    print('Choose a door to claim your third weapon')
                    if getweaponright(rightdoor) == 'left':
                        print('Try again')
                        hero = 0
                    else:
                        hero += 25
                        if hero == 100:
                            finalboss = int(input('Press 4 to slay the final boss: '))
                            print('You win, you have used all of your weapons to slay the final boss')







