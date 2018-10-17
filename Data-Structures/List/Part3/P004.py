"""
Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number. 
Note: In mathematics, the sieve of Eratosthenes, 
(Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) 
one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
"""

def prime_eratosthenes(n):
    nprime_list = []
    prime_list = []
    for i in range(2, n+1):
        if i not in nprime_list:
            prime_list.append(i)
            for j in range(i*i, n+1, i):
                nprime_list.append(j)
    return prime_list

print(prime_eratosthenes(30))
#include("../../new_editor/editor_python.php")
