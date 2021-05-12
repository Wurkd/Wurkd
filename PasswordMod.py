word = input()
password = ''

for i in word:
    if i == 'i':
        print(i)
        password += '!'
    elif i == 'a':
        password += '@'
    elif i == 'm':
        password += 'M'
    elif i == 'B':
        password += '8'
    elif i == 'o':
        password += '.'
    else:
        print(i)
        password += i
password = (password + 'q*s')
print(password)

#Adding file to Git