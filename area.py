name = input('Pls enter your name: ')
print(name,', ')
score = float(input('Pls enter your score: '))
if score >= 101:
    print(name, ', Score above the normal range, Invalid score!!!')
elif score >= 70:
    print(name, ', You have Distinction')
elif score >= 60:
    print(name, ', You have Credit')
elif score >= 50:
    print(name, ', You have Merit')
elif score >= 45:
    print(name, ', You have PAss')
elif score >= 0:
    print(name, ', You have Failed')
else:
    print(name, ', Score below the normal range, Invalid Score!!!')

print('Goodbye, See you later!!!')