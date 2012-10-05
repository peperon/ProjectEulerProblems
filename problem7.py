def is_prime(primes, number):
    for i in primes:
        if number % i == 0:
            return False
    return True

def problem7():
    primes = [2, 3, 5, 7, 11]
    number = 13
    while len(primes) < 10001:
        if is_prime(primes, number):
            primes.append(number)
        number += 1
    return primes[-1]

if __name__ == "__main__":
    print(problem7())
