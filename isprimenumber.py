num = 20

# If given number is greater than 1
if num > 1:

    # Iterate from 2 to n / 2
    for i in range(2 , num // 2):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num , "is not a prime number")
            break
    else:
        print(num , "is a prime number")

else:
    print(num , "is not a prime number")



add = lambda x,y : x +y
sqr = lambda a: a * a

result1 = sqr(5)
result = add(40,50)


