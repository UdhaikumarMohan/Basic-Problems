# Swap Two Variables without causing overflow:

def swap(a,b):

    a = a ^ b
    b = b ^ a
    a = a ^ b

    print(a)
    print(b)

a = 6
b = 5

swap(a,b)