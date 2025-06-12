'''
Task 2: Sum of Integers from 1 to 50 Using a Loop

Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.

'''

ary=list(range(1,51))

#print(ary)
a=0
for x in ary :
   a=a+x

print('The Sum of numbers from 1 to 50 is :',a)