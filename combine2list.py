def combineList(a, b):
    for i in b:
        a.append(i)
    return a

A = int(input('Enter the length of the first list: '))
a = []
for i in range(A):
    item = input('Enter item: ')
    a.append(item)

B = int(input('Enter the length of the second list: '))
b = []
for i in range(B):
    item = input('Enter item: ')
    b.append(item)

print('The combined list is:')
print(combineList(a,b))
