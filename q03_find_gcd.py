#q03_find_gcd

from fractions import gcd

while True:
    #function gcd(m, n)
    def gcd(m, n):
        if m > n:
            m, n = n, m

        for x in range (m, 0, -1):
            if m % x == 0 and n % x == 0:
                return x
    #get input
    m = int(input("Enter a number: "))
    n = int(input("Enter a number: "))

    #get gcd
    print(str(gcd(m, n)))
    print("Congratulation! You got your gcd.")
