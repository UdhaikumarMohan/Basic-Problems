# Conert Celcius to fahrenheit:

def fahr(Celcius):

    result = (Celcius*(9/5)) + 32 

    fahrenheit = "{} *C is equal to {} *F"

    return (fahrenheit.format(Celcius,result))

Celcius = float(input("Enter the value in *C: "))

print(fahr(Celcius))


