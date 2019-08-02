# Python Program to Swap Two Variables

def swap(A,B):

    temp = B

    B = A

    A = temp

    print(A,B)


A = 5

B = 6

swap(A,B)