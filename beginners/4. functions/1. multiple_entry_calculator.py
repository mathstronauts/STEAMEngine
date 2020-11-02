#print greetings
print('Welcome to my simple calculator!')
print('You get 3 calculations!')

#get user inputs
print('This is your first calculation entry!')
first_num1 = input('Please enter first integer: ')
operation1 = input('Please enter operation(+,-,*,/): ')
second_num1 = input('Please enter second integer: ')

if(operation1 == '+'):    
    #sum the two numbers
    result = int(first_num1) + int(second_num1)

    #output the result to the user
    print('The sum of the two numbers is', result)
elif(operation1 == '-'):    
    #subtract the two numbers
    result = int(first_num1) - int(second_num1)

    #output the result to the user
    print('The difference of the two numbers is', result)
elif(operation1 == '*'):    
    #multiply the two numbers
    result = int(first_num1) * int(second_num1)

    #output the result to the user
    print('The product of the two numbers is', result)
elif(operation1 == '/'):    
    #sum the two numbers
    result = int(first_num1) / int(second_num1)

    #output the result to the user
    print('The quotient of the two numbers is', result)
else:
    print('Sorry operation is not recognized!')

#get user inputs
print('This is your second calculation entry!')
first_num2 = input('Please enter first integer: ')
operation2 = input('Please enter operation(+,-,*,/): ')
second_num2 = input('Please enter second integer: ')

if(operation2 == '+'):    
    #sum the two numbers
    result = int(first_num2) + int(second_num2)

    #output the result to the user
    print('The sum of the two numbers is', result)
elif(operation2 == '-'):    
    #subtract the two numbers
    result = int(first_num2) - int(second_num2)

    #output the result to the user
    print('The difference of the two numbers is', result)
elif(operation2 == '*'):    
    #multiply the two numbers
    result = int(first_num2) * int(second_num2)

    #output the result to the user
    print('The product of the two numbers is', result)
elif(operation2 == '/'):    
    #sum the two numbers
    result = int(first_num2) / int(second_num2)

    #output the result to the user
    print('The quotient of the two numbers is', result)
else:
    print('Sorry operation is not recognized!')
    
#get user inputs
print('This is your last calculation entry!')
first_num3 = input('Please enter first integer: ')
operation3 = input('Please enter operation(+,-,*,/): ')
second_num3 = input('Please enter second integer: ')

if(operation3 == '+'):    
    #sum the two numbers
    result = int(first_num3) + int(second_num3)

    #output the result to the user
    print('The sum of the two numbers is', result)
elif(operation3 == '-'):    
    #subtract the two numbers
    result = int(first_num3) - int(second_num3)

    #output the result to the user
    print('The difference of the two numbers is', result)
elif(operation3 == '*'):    
    #multiply the two numbers
    result = int(first_num3) * int(second_num3)

    #output the result to the user
    print('The product of the two numbers is', result)
elif(operation3 == '/'):    
    #sum the two numbers
    result = int(first_num3) / int(second_num3)

    #output the result to the user
    print('The quotient of the two numbers is', result)
else:
    print('Sorry operation is not recognized!')
    
print('Thank you for using my simple calculator!')
