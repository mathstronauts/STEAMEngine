def calculator(num1,num2,operation):
    if(operation == '+'):    
        #sum the two numbers
        result = int(num1) + int(num2)
    
        #output the result to the user
        print('The sum of the two numbers is', result)
    elif(operation == '-'):    
        #subtract the two numbers
        result = int(num1) - int(num2)
    
        #output the result to the user
        print('The difference of the two numbers is', result)
    elif(operation == '*'):    
        #multiply the two numbers
        result = int(num1) * int(num2)
    
        #output the result to the user
        print('The product of the two numbers is', result)
    elif(operation == '/'):    
        #sum the two numbers
        result = int(num1) / int(num2)
    
        #output the result to the user
        print('The quotient of the two numbers is', result)
    else:
        print('Sorry operation is not recognized!')

#print greetings
print('Welcome to my simple calculator!')
print('You get 3 calculations!')

#get user inputs
print('This is your first calculation entry!')
first_num1 = input('Please enter first integer: ')
operation1 = input('Please enter operation(+,-,*,/): ')
second_num1 = input('Please enter second integer: ')

#perform calculation
calculator(first_num1,second_num1,operation1)

#get user inputs
print('This is your second calculation entry!')
first_num2 = input('Please enter first integer: ')
operation2 = input('Please enter operation(+,-,*,/): ')
second_num2 = input('Please enter second integer: ')

#perform calculation
calculator(first_num2,second_num2,operation2)
    
#get user inputs
print('This is your last calculation entry!')
first_num3 = input('Please enter first integer: ')
operation3 = input('Please enter operation(+,-,*,/): ')
second_num3 = input('Please enter second integer: ')

#perform calculation
calculator(first_num3,second_num3,operation3)
    
print('Thank you for using my simple calculator!')
