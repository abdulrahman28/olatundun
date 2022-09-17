print('This program computes the perimeter of shapes')
print('1. Square    2. Rectangle')
opt = input('Enter your option: ')
if opt == '1':
    print('Square shape selected!!!')
    l = float(input('Enter the Length of the square (m): '))
    per = 4 * l
    print('The perimeter of the sqyare =', per, 'm')
elif opt == '2':
    print('Rectangle shape selected!!!')
