import prime

#list1= {10 , 20 , 30 , 40 , 11 , 21 , 50 , 60}
#for i in range(0, len(list1)):
    #if i % 2 == 0:
     #print(list1[i])

#list1= [10, 20, 30, 40,11, 21, 50, 60]
#for i in range(0, len(list1)):
    #if i % 2 == 1:
     #print(list1[i])


#list1= [10, 20, 30, 40,11, 21, 50, 60]
#for i in range(0, len(list1)):
    #if list1[i] % 2 == 0 :
     #print(list1[i])



#list1= [10, 20, 30, 40,11, 21, 50, 60]
#for i in range(0, len(list1)):
    #if list1[i] % 2 == 1 :
     #print(list1[i])

#list1 = [10 , 20 , 30 , 40 , 11 , 21 , 50 , 60]
#for i in range(1 , len(list1)):
    #if prime.is_prime_number(i) :
        #print(list1[i])


#list1 = [10, 20, 30, 40, 11, 21, 50, 60]
#total = 0
#for i in range(0, len(list1)):
    #total = total + list1[i]
#print(total)


#
# APPEND: Adds an element at the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# CLEAR:Removes all the elements from the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# COPY :Returns a copy of the list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)



# POP :Removes the element at the specified position

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# REMOVE: Removes the item with the specified value

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


l1a1 = [10, 20, -10, -40, 30, -70, 60]

en = []
on = []

for index in range (0, len(l1a1)):
    if l1a1[index] % 2 ==0:
        en.append(l1a1[index])
    else:
        on.append(l1a1[index])