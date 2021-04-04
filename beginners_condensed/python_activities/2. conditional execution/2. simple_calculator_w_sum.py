#print greetings
print('Welcome to my simple calculator!')

#get user inputs
first_num = input('Please enter first integer: ')
operation = input('Please enter operation(+,-,*,/): ')
second_num = input('Please enter second integer: ')

#use if/else for first demo (just with sum operation)
if(operation == '+'):    
    #sum the two numbers
    result = int(first_num) + int(second_num)

    #output the result to the user
    print('The sum of the two numbers is', result)

else:
    print('Sorry operation is not recognized!')
