def absolute_value(num):
	"""This function returns the absolute
	value of the entered number"""

	if num >= 0:
		return num
	else:
		return -num

# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))






#In this program we will see how to define a class

class MyFirstClass():
    #Class Attributes
    var = 10

firstObject = MyFirstClass()
print(firstObject)      #Printing object's memory hex
print(firstObject.var)  #Accessing Class Attributes

secondObject = MyFirstClass()
print(secondObject)
print(secondObject.var)


def calculate(a,b):
    print("The sum", a+b)
    print("The difference", a-b)
    print("The product", a*b)
calculate(5,6)



def my_function():
  print("Hello from a function")

my_function()
