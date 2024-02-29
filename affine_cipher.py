import sys
import string
import platform

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def are_coprime(a, m):
    # Returns true if gcd=1.
    return gcd(a, m) == 1

def keyinverse(a, m):
    """
        keyinverse(a, m) -> int
        Finds the modular inverse of 'a' modulo 'm' if 'a' is coprime to 'm'.
        Raises a ValueError if the inverse does not exist.
        Returns the computed modular inverse.
    """
    if not are_coprime(a, m):
        raise ValueError("The 'a' value must be coprime to 26.")
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("Inverse does not exist for the given 'a' value.")

def calcenc(c, a, b):
    """
        calcenc(c, a, b) -> int
        Performs encryption for a single character using the Affine Cipher formula.
        Returns the encrypted character's index in the alphabet.
    """
    return (a * c + b) % 26
