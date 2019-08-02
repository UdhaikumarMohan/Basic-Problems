# Python Program to Swap Two Variables without using temporary variable:

def swap_temp(A,B):

    A,B = B,A
    print(A,B)

A = 5
B = 6
swap_temp(A,B)