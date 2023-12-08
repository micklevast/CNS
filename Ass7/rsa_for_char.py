# RSA Integer

import gmpy2
from random import getrandbits
from sympy import isprime

# Function to generate a random 30-bit prime number
def generate_small_prime():
    while True:
        num = gmpy2.mpz(getrandbits(30))
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

def find_gcd(num1, num2):
    return gmpy2.gcd(num1, num2)

def generate_rsa_key_pair():
    p = generate_small_prime()
    q = generate_small_prime()

    print("Small prime numbers:\n\tp = ", p, "\n\tq = ", q)

    n = p * q
    print("n = ", n)
    phi = (p - 1) * (q - 1)
    print("phi = ", phi)

    e = gmpy2.mpz(65537) 
    print("e = ",e)

    d = mod_inverse(e, phi)
    print("d = ",d)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def encrypt_message(public_key, message):
    e, n = public_key
    encrypted_message = [pow_m(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt_message(private_key, ciphertext):
    d, n = private_key
    decrypted_message = ''.join([chr(pow_m(char, d, n)) for char in ciphertext])
    return decrypted_message

if __name__ == "__main__":
    public_key, private_key = generate_rsa_key_pair()

    message = input("Enter your message: ")
    
    print("Public key:", public_key)
    print("Private key:", private_key)

    ciphertext = encrypt_message(public_key, message)
    print("Encrypted Message:", ciphertext)

    decrypted_message = decrypt_message(private_key, ciphertext)
    print("\nDecrypted Message:", decrypted_message)