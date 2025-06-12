
'''
Task 1:
    Check if a Number is Even or Odd
    Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.

'''

val=int(input('Enter a number : '))

if(val % 2 == 0) :
    print(val ,'is an even number.')
else : #if(val % 2 > 0) :
    print(val ,'is an odd number')

#print('thanks')