import random
from sympy import mod_inverse

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    print(f"Step 1: n = p * q = {n}")
    print(f"Step 2: φ(n) = (p-1) * (q-1) = {phi}")

    e = choose_public_exponent(phi)
    d = mod_inverse(e, phi)

    print(f"Step 3: Choose public exponent (e): {e}")
    print(f"Step 4: Calculate private exponent (d) using modular inverse: {d}")

    # Print values
    public_key = (n, e)
    private_key = (n, d)
    print(f"\nPublic Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")

    return public_key, private_key

def choose_public_exponent(phi):
    e_values = [65537, 257, 17, 5, 3]
    for e in e_values:
        if 1 < e < phi and gcd(e, phi) == 1:
            return e
    raise ValueError("Unable to find a suitable public exponent (e). Try different p and q values.")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def encrypt(message, public_key):
    n, e = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text

def decrypt(cipher_text, private_key):
    n, d = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(decrypted_message)

def main():
    p = int(input("Enter the value of p: "))
    q = int(input("Enter the value of q: "))

    print("\nKey Generation:")
    public_key, private_key = generate_keypair(p, q)

    message = input("\nEnter a message to encrypt: ")

    cipher_text = encrypt(message, public_key)
    print(f"Ciphertext: {cipher_text}")

    decrypted_message = decrypt(cipher_text, private_key)
    print(f"Decrypted message: {message}")

if __name__ == "__main__":
    main()
