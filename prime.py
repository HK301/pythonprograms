def is_prime_number(number):
    if number < 1:
        print("Invalid input.")
        raise ValueError("Value must be greater than 1.")
    count = 0;
    for i in range(1, number+1):
        if number % i == 0:
            count = count + 1

    if count == 2:
       return True
    else:
        return False