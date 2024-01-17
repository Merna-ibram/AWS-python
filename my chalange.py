def is_prime(number):

    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def primes(start, end):
    myprimes = [num for num in range(start, end + 1) if is_prime(num)]

    for prime in myprimes:
        print(prime)

if __name__ == "__main__":
    start_num = 1
    end_num = 250

    primes(start_num, end_num)
