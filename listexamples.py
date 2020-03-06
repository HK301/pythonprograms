# Python program to print list
# using for loop
a = [1, 2, 3, 4, 5]

# printing the list using loop
for x in range(len(a)):
    print(a[x])

# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        print(num, end=" ")



# # Python program to print odd Numbers in a List



list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 1:
        print(num, end=" ")






# Python3 code to demonstrate
# Separating odd and even index elements
# using naive method

# initializing list
test_list = [3, 6, 7, 8, 9, 2, 1, 5]

# printing original list
print("The original list : " + str(test_list))

# using naive method
# Separating odd and even index elements
odd_i = []
even_i = []
for i in range(0, len(test_list)):
    if i % 2:
        even_i.append(test_list[i])
    else:
        odd_i.append(test_list[i])

res = odd_i + even_i

# print result
print("Seprated odd and even index list: " + str(res))





def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1

input_str = 'ABç∂EF'

if __name__ == "__main__":
    print('Reverse String using while loop =', reverse_while_loop(input_str))

    # Python code to demonstrate
    # to construct alternate element list
    # using list comprehension

    # initializing list
    test_list = [1, 4, 6, 7, 9, 3, 5]

    # printing original list
    print("The original list : " + str(test_list))

    # using list comprehension
    # to construct alternate element list
    res = [test_list[i] for i in range(len(test_list)) if i % 2 != 0]

    # printing result
    print("The alternate element list is : " + str(res))

# Python3 code to demonstrate
# to get index and value
# using naive method

# initializing list
test_list = [1, 4, 5, 6, 7]

# Printing list
print("Original list is : " + str(test_list))

# using naive method to
# get index and value
print("List index-value are : ")
for i in range(len(test_list)):
    print(i, end=" ")
    print(test_list[i])



# program to sCalculate Sum & Average of an Array
x = 10
y = 20
z = 30
sum = (x+y+z)
avg = (x+y+z /3)
print(sum, avg)
