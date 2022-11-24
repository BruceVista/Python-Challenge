
number_1 = input('first number: ') 
   

number_2 = int(input('second number: '))

operation = input('operator: ')
if operation == '+':  
         print('{} + {} = '.format(number_1, number_2))
         print(number_1 + number_2)
elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
elif operation == '*':
         print('{} * {} = '.format(number_1, number_2))
         print(number_1 * number_2) 
elif operation == '/':
         print('{} / {} = '.format(number_1, number_2))
         print(number_1 / number_2)

    


 