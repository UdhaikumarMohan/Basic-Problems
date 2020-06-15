'''
# Write a program to check the given year is leap year or not:

def is_leap(year):

    if year<=0:
        
        return("Year cannot be a negative value")

    elif year%4==0 and year%400==0 :

        if year%100==0 :

            flag = True

    elif year%4==0 :

        flag = True

    else:

        flag = False

    return flag

year = 2100
print(is_leap(year))
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + str(self.age))

p1 = Person("John", 36)
p2 = Person("jog",76)
p1.myfunc() 
p2.myfunc()            