def exponent(base, index):
    product = 1
    for i in range(index):
        product = product*base
    return product

#print greetings
print('Welcome to my advance calculator!')

#get user inputs
operation = input('Please enter operation(+,-,*,/,**): ')
if (operation == '**'):
    base = input('Please enter base integer: ')
    exp = input('Please enter integer exponent: ')
else:
    first_num = input('Please enter first integer: ')
    second_num = input('Please enter second integer: ')

if(operation == '+'):    
    #sum the two numbers
    result = int(first_num) + int(second_num)

    #output the total to the user
    print('The sum of the two numbers is', result)
elif(operation == '-'):    
    #subtract the two numbers
    result = int(first_num) - int(second_num)

    #output the total to the user
    print('The difference of the two numbers is', result)
elif(operation == '*'):    
    #multiply the two numbers
    result = int(first_num) * int(second_num)

    #output the total to the user
    print('The product of the two numbers is', result)
elif(operation == '/'):    
    #sum the two numbers
    result = int(first_num) / int(second_num)

    #output the total to the user
    print('The quotient of the two numbers is', result)

elif(operation == '**'):    
    #sum the two numbers
    result = exponent(int(base), int(exp))

    #output the total to the user
    print('The power of', base, 'to the index of', exp, 'is', result)
    
else:
    print('Sorry operation is not recognized!')
    
print('Thanks for using my advance calculator')
