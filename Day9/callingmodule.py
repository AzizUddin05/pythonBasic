import module1 as m
import os

while True :
    os.system('cls')
    print('    Main Menu    ')
    print('-'*20)
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')
    print('Enter your selection : ', end='')
    ch = input()
    if ch == '1':
        
        x = int(input('Enter first value : '))
        y = int(input('Enter second value : '))

        results = m.add(x,y)
        print(f'addition is {results}')
       
    elif ch == '2':
        x = int(input('Enter first value : '))
        y = int(input('Enter second value : '))

        results = m.sub(x,y)
        print(f'subtraction is {results}')
        
    elif ch == '3':
        x = int(input('Enter first value : '))
        y = int(input('Enter second value : '))

        results = m.mult(x,y)
        print(f'multiplication is {results}')
        
    elif ch == '4':
        x = int(input('Enter first value : '))
        y = int(input('Enter second value : '))

        results = m.div(x,y)
        print(f'division is {results}')
        
    elif ch == '5':
        break
    else:
        print('Sorry invallid selection')

    print('Press enter to continue .....')
    input()
