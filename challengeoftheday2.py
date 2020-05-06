#!/usr/bin/env python3

factorial = 1

#User input
num = int(input("Please enter a number: "))

#Determining factorial
if num < 0:
    print("Sorry, factorials do not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1") 
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("The factorial of ",num," is ",factorial)
       