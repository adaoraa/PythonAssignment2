#Adaora Atuegbu
#CSCE 222-502
#Lee
#Atuegbu-Adaora-EC-hw1


def gcd(a, b):  # this function will compute the gcd of integer arguments a and b
    if int(b == 0):
        return int(a)
    else:
        return gcd(int(b), int(a) % int(b))


def A(m, n, s="%s"):  # Ackermann function defined
    print(s % ("A(%d, %d)" % (m, n)))
    if m == 0:
        return n+1
    elif n == 0:
        return A(m-1, 1, s)
    n1 = A(m, n-1, s % ("A(%d, %%s)" % (m-1)))
    return A(m-1, n1, s)


#  gcd and Ackermann functions will be called here
loops = 1  # set to 1 because based on instruction, invocation includes self (Ackermann's arguments)
while True:
    #  When gcd function is called
    a = 12
    b = 15
    print("the first argument is ", a)
    print("the second argument is ", b)
    print("The greatest common denominator of these 2 integers is as follows: ")
    print(gcd(a, b))
    #  When Ackermann function is called
    m = 1
    n = 1
    print("the first argument is ", m)
    print("the second argument is ", n)
    print("The Ackermann function for these arguments is as follows: ")
    #  for loop to determine how many times Ackermann function invoked
    for i in range(A(1, 1)):
        loops += 1
    print('The Ackermann function was invoked', loops, 'times')
    break

