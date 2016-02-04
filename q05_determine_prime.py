#q05_determine_prime.py


# Python program to check if the input number is prime or not

# take input from the user
number = int(input("Enter a number: "))

def is_prime(number):
    if number < 2:
        print("{0} is not a prime number.".format(number))
    if number== 2:
        print("{0} is a prime number.".format(number))
    else:
        for div in range(2,number):
            if number % div == 0:
                return False
        print("{0} is not a prime number.".format(number))


