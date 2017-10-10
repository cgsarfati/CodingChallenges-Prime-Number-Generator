"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def is_prime(num):

    # consider edge cases 1st: 0, 1, 2

    # 0, 1, not prime
    if num < 2:
        return False

    # 2 is prime
    if num == 2:
        return True

    # even #s not prime
    if num % 2 == 0:
        return False

    # rest of nums: check if any odd number b/w 3 and sqrt(num)
    # that evenly divides num

    n = 3

    while n * n <= num:
        if num % n == 0:
            return False
        n += 2

    return True


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    # store lst of prime numbers to be returned @ end
    primes = []

    # set up prime # generator from other fn starting at 2
    num = 2

    while count > 0:

        # check if prime
        if is_prime(num):
            # if so, append to primes lst
            primes.append(num)
            # decrement by 1; used to keep track of how many primes enter lst
            count -= 1

        # check next number if prime, etc.
        num += 1

    # return final lst
    return primes

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
