# Write a python program to check the Number is odd or even:

def Odd_even(Num):

    if Num%2==0:

        result = "It is an even number"

    else: 

        result = "It is not an even number"

    return result

# Input

Num = int(input("Enter the number: "))
print(Odd_even(Num))
