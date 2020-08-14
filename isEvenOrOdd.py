def isEven(num):
    if num == 0:
        print('number must be a positive integer')
    elif num == 2 or num % 2 == 0:
        print('even')
    else:
        print('odd')


isEven(int(input()))

