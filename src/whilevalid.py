name = ''
while name != 'jason balladares':
    print('please type your name.')
    name = input()
print('Thank you!')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
