#q06_display_matrix

#import random
import random

#function
def print_matrix(n):
    if n < 1:
        print("Error! Number must not be less than 1!")
    else:
        for j in range (n):
            for i in range (n):
                print("{0:<3}".format(random.randint(0,1)), end="")
            print()

#print matrix               
print_matrix(int(input("enter an integer: ")))

        
