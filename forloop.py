n = int(input('Enter the number of numbers: '))
j = 0
for i in range(1,n+1):
    a = float(input('Enter number: '))
    j = j + a
print('Sum = ' + str(j))
print('Average = ' + str(j/n))