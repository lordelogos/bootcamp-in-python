def frame(arr):
    l = len(max(arr, key=len))
    print('*' * (l+4))
    for i in range(len(arr)):
        print('* ' + arr[i].ljust(l) + ' *')
    print('*' * (l+4))

A = int(input('Enter the number items in the list: '))
a = []
for i in range(A):
    item = input('Enter item: ')
    a.append(item)
    
frame(a)
