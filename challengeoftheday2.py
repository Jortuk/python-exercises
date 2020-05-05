#!/usr/bin/env python3

factorial = 1

#While session is True, input will be asked for again after the answer until file is closed (Crtl + C)
session = True
while session:

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
       