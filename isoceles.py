def isoceles(n):
    l = (2*n) - 1
    for i in range(1, l+1, 2):
        a = '#' * i
        print(a.center(l))

isoceles(int(input('Enter length of Triangle: ')))
        
    
