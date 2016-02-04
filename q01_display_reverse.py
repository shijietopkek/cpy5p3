#q01_display_reverse.py

#while loop
while True:

    #get input
    n = int(input("Enter number: "))

    #function
    def reverse_int(n):
      rev = 0
      while(n > 0):
        rev = (10 * rev) + n % 10
        n //= 10
      return rev

    #generate output
    print(reverse_int(n))
