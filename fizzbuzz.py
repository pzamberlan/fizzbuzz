for i in xrange(1, 101): #cuenta los numeros del 1 al 100
    if i % 15 == 0: #si el resto de la division es = a 0 imprime fizzbuzz
        print "FizzBuzz"
    elif i % 3 == 0:#si el resto de la division es = a 0 imprime fizz
        print "Fizz"
    elif i % 5 == 0:#si el resto de la division es = a 0 imprime buzz
        print "Buzz"
    else:
        print i
