#!/usr/bin/python3
"""Defining a function isWinner"""


def is_prime(n):
    """Returns true if n is a prime number else False"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(n):
    """Counts the number of prime numbers up to n"""
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count


def isWinner(x, nums):
    """Returns the winner of the prime game of numbers"""
    if x < 1 or not nums:
        return None

    maria_ws = 0
    ben_ws = 0
    for n in nums:
        primes_count = count_primes(n)
        if primes_count % 2 == 0:
            ben_ws += 1
        else:
            maria_ws += 1

    if maria_ws > ben_ws:
        return 'Maria'
    elif ben_ws > maria_ws:
        return 'Ben'
    return None
