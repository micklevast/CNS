# RSA Integer

import gmpy2
from random import getrandbits
from sympy import isprime

# Function to generate a random 100-digit prime number
def generate_large_prime():
    while True:
        num = gmpy2.mpz(getrandbits(300))
        
        if isprime(num):
            return num

# Function to compute the modular inverse
def mod_inverse(a, m):
    g, ans_s, ans_t = gmpy2.gcdext(a, m)
    if g != 1:
        print("Inverse doesn't exist")
        return 0
    else:
        res = gmpy2.invert(a, m)
        return res

# Function to perform modular exponentiation
def pow_m(a, b, n):
    return gmpy2.powmod(a, b, n)

# Function to find the greatest common divisor
def find_gcd(num1, num2):
    return gmpy2.gcd(num1, num2)

# Function to generate RSA key pair
def generate_rsa_key_pair():
    p = generate_large_prime()
    q = generate_large_prime()

    print("Large prime numbers:\n\tp = ",p,"\n\tq = ",q)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = gmpy2.mpz(65537)  # Common public exponent

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

# Function to encrypt a message
def encrypt_message(public_key, message):
    e, n = public_key
    message = gmpy2.mpz(message)
    return pow_m(message, e, n)

# Function to decrypt a message
def decrypt_message(private_key, ciphertext):
    d, n = private_key
    ciphertext = gmpy2.mpz(ciphertext)
    return pow_m(ciphertext, d, n)

if __name__ == "__main__":
    public_key, private_key = generate_rsa_key_pair()

    message = gmpy2.mpz(input("Enter your message (as an integer): "))
    
    print("Public key:", public_key)
    print("Private key:", private_key)

    ciphertext = encrypt_message(public_key, message)
    print("Encrypted Message:", ciphertext)

    decrypted_message = decrypt_message(private_key, ciphertext)
    print("Decrypted Message:", decrypted_message)