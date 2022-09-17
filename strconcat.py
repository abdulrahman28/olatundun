print('The program computes Quadratic Equation (ax^2+bx+c=0)')

a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))

d = b**2 - (4 * a * c)

if d < 0:
    d = (-d) ** 0.5
    re = -b / (2*a)
    im = d / (2*a)
    print('x = ' + str(re) + ' + j' + str(im))
    print('x = ' + str(re) + ' - j' + str(im))
elif d == 0:
    d = -b / (2*a)
    print('x = ' + str(d))
    print('x = ' + str(d))
else:
    d = d ** 0.5
    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)
    print('x = ' + str(x1))
    print('x = ' + str(x2))