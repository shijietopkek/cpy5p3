#q07_convert_ms

#function
def convert_ms(n):
    if n < 0:
        print("Invalid Input.")
    else:
        if (n // 1000) < 60:
            print("0:0:{0}".format(n // 1000))
        elif (n // 1000) > 59 and (n // 1000) < 3600:
            print("0:{0}:{1}".format((n // 1000) // 60, ((n // 1000) - 60 * ((n // 1000) // 60))))
        else:
            print("{0}:{1}:{2}".format((n // 1000) // 3600, ((n // 1000) % 3600) // 60 , (n // 1000) % 60))

#get input
convert_ms(int(input("Enter time in miliseconds: ")))
