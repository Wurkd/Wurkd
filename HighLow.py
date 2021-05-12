answer = int(23) #set an answer to your high low game

lowBound = int(input('Enter the lower bound:')) #get a number to show what the low bound is
highBound = int(input('Enter the higher bound:')) #get a number to show what the high bound is

guess = int(input('Great, now guess a number between the highest and lowest bound:')) let user

while guess != answer:
    if guess < answer:
        print('too low')
        guess = int(input('Try again'))
    elif guess > answer:
        print('too high')
        guess = int(input('Try again'))
print('right')
