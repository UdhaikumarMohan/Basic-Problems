# Write a python program to check a number is positive or negative or zero:

def Number(Num):

    if Num == 0:

        Status = "It is Zero"

    elif Num<0:

        Status = "It is Negative Number"

    else:

        Status = "It is Positive Number"

    return Status

Num = float(input("Enter the Integer: "))
print(Number(Num))


