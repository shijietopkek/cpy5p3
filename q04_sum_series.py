#q04_sum_series

#print heading
print("{0:<8}{1}".format("i","m(i)"))

#function
def m_series(i):
    result = 0
    for j in range(1, i+1):
        result += j/(j+1)
    return result

#generate table
for i in range(1, 21):
    print("{0:<8}{1:.4f}".format(i, m_series(i)))
