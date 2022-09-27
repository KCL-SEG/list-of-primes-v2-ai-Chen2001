def primes(number_of_primes):
    if number_of_primes<=0:
        raise ValueError(f"the number of primes must be positive")
    list = []
    number=2
    while len(list)<number_of_primes:
        n=2
        while n*n<number:
            if number%n!=0:
                n+=1
            else:
                break
        if n*n>number:
            list.append(number)
        number+=1       
    return list