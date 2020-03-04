def genPrimes():
    listp,prime = [2,3],2
    yield prime
    prime = 3
    yield prime
    while True:
        a = 0
        try:
            while prime % listp[a] != 0:
                a += 1
            prime += 2
        except IndexError:
            yield prime
            listp.append(prime)
