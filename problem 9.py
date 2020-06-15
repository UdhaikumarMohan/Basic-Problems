# convert Kilometer into miles:

def miles_km(Km):

    if Km >= 0 :

        factor = 0.621371

        result = Km*factor

        miles = ("%0.3f Kilometers is equal to %0.3f miles" %(Km,result))

        #result = "{} kilometer is equal to {} miles."
        #return (result.format(Km,miles))

    else:

        miles = "Kilometer should not be in Negative Value: "

    return miles

Km = float(input("Enter the Distance: "))
print(miles_km(Km))







    