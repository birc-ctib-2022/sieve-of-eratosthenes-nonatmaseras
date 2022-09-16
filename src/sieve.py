"""Computing primes."""


from os import remove


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0    
    # 2 is a prime number
    primes = [2]
    #iterate over 3 to n+1
    for candidate in list(range(3, n + 1)):
        #calculate the residuals --> if any number is divisible (residual == 0), then it is not prime
        if all(candidate % p != 0 for p in primes):
            primes.append(candidate)
        
        
    return primes

