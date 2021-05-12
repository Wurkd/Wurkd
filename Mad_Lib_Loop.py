# Temi
#
# IT 140
#
# 3/28
#
# # a program that loops madlibs till you print quit

string = input()

while string != 'quit 0':
    words = string.split()
    print('Eating',words[1], words[0],'a day keeps the doctor away.')
    string = input()

    # while inti != 0:
    #     num = inti
    #     print('Eating',num, string,'a day keeps the doctor away.')