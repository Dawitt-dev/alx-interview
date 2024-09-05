#!/usr/bin/python3
""" THE PRIME GAME"""

def sieve_of_eratosthenes(n):
    """ func to find all primes up to n using Sieve of Eratosthenes """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for multiple in range(i*i, n + 1, i):
                sieve[multiple] = False
    primes = [i for i in range(2, n + 1) if sieve[i]]
    return primes


def isWinner(x, nums):
    """ Determines the winner of the prime game """
    if x < 1 or not nums:
        return None

    # Precompute primes up to the maximum number in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Prepare to count wins
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_game = [p for p in primes if p <= n]
        turn = 0  # Maria starts first, turn is even for Maria and odd for Ben
        while primes_in_game:
            prime = primes_in_game.pop(0)
            primes_in_game = [p for p in primes_in_game if p % prime != 0]
            turn += 1

        if turn % 2 == 0:
            ben_wins += 1  # Ben wins if the turn count is even
        else:
            maria_wins += 1  # Maria wins if the turn count is odd

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
