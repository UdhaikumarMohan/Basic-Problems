#Python Program to calculate the area of triangle:

# Base and Height are the Parameters Belong to the Triangle:

Base=float(input("Enter the Base of the Triangle: "))
Height=float(input("Enter the Height of the Triangle: "))

# Area of the Triangle is 1/2(Base*Height). In meters

def area_triangle(Base,Height):

    if Base>0 or Height>0:

        Area= (Base*Height)/2

    else:

        Area = "Invalid Measurements"

    return (Area)

print("The Area of Triangle is", area_triangle(Base,Height))