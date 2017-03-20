for number in range(2, 200000):
    for number2 in range(2, number):
        if number % number2 == 0:
            print "This is not a prime number " + str(number)
            break;
        else:
            print "This is a prime number " + str(number)
            break;
