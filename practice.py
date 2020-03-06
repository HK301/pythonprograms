# Program to check eligibility for voting.
user_age = 14

if user_age >= 18:
    print("user is eligible for voting")
else:
    print("user is not eligible for voting")


for i in range(2, 11):
    print(i)

i = 2
while i < 11:
    print(i)
    i = i + 1

def greet(name):
    print("Hello, Mr."+ name + " Welcome to Pioneer Coders!")

greet("Krishna") # funciton calling.

def add(x,y):
  result =  x + y;
  return result;
sum = add(10,20)
print(sum)


def simple_interest(principal, no_of_years, rate_of_interest):
    si = (principal * no_of_years * rate_of_interest) / 100
    return si

P = float(input("Enter the principal amount : "))
N = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))
interest_amount = simple_interest(P, N, R)
print("Simple interest : {}".format(interest_amount))


# fibonacci series: 0 1 1 2 3 5 8 etc
def fibonacci_using_loop(number):
    if number == 0: return 0
    fibonacci0, fibonacci1 = 0, 1
    print(fibonacci0)
    print(fibonacci1)
    for i in range(2, number + 1):
        fibonacci1 = fibonacci0 + fibonacci1
        fibonacci0 = fibonacci1
        print(fibonacci1)

if __name__ == '__main__':
    userInput = int(input('Enter the number up to which you wish to calculate fibonnaci series: '))
    fibonacci_using_loop(userInput)