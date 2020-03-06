#  Print 1 to 10 numbers

for i in range(10):
    print(i)

# Print 10 to 1 numbers

for i in range(10-1, 0, -1):
    print(i)



# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

# checking

    if num % 2 == 0:

        print(num, end=" ")

# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 1:
        print(num, end=" ")

# Python program to print all
# prime number in an interval

start = 11
end = 25

for val in range(start, end + 1):

    # If num is divisible by any number
    # between 2 and val, it is not prime
    if val > 1:
        for n in range(2, val):


            if (val % n) == 0:
                break
        else:
            print(val)

# Python program to print all EVEN numbers within an interval
l = 10
u = 20

for num in range(l, u + 1, 2):
    print(num)



lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
for i in range (lower,upper+1):
    if(i%7==0):
        print(i)


