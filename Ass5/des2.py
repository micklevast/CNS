from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    # Pad the plaintext to a multiple of 8 bytes (64 bits)
    padded_plaintext = plaintext.ljust((len(plaintext) + 7) // 8 * 8, b'\0')
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.rstrip(b'\0')

# Example usage
if __name__ == "__main__":
    key = get_random_bytes(8)  # Generate a random 64-bit (8-byte) key
    print('\n*** Data Encryption Standard Algorithm ***')

    # Prompt the user for input and store it in a variable
    plaintext = input("Enter a string: ").encode()  # Convert user input to bytes

    ciphertext = encrypt(plaintext, key)
    decrypted_text = decrypt(ciphertext, key)

    print("Original plaintext:", plaintext.decode())  # Decode to display as a string
    print("Encrypted ciphertext:", ciphertext)
    print("Decrypted plaintext:", decrypted_text.decode())  # Decode to display as a string
