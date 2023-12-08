from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import time

def generate_rsa_key_pair(key_size=2048):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    return private_key

def save_rsa_keys(private_key, public_key):
    timestamp = time.strftime("%Y%m%d%H%M%S")
    private_key_filename = f"private_key_{timestamp}.pem"
    public_key_filename = f"public_key_{timestamp}.pem"
    
    with open(private_key_filename, "wb") as private_key_file:
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        private_key_file.write(private_pem)
    
    with open(public_key_filename, "wb") as public_key_file:
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        public_key_file.write(public_pem)

    return private_key_filename, public_key_filename

def load_rsa_private_key(filename):
    with open(filename, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())
    return private_key

def load_rsa_public_key(filename):
    with open(filename, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())
    return public_key

def encrypt_message(public_key, message):
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt_message(private_key, ciphertext):
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message

if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Generate RSA Key Pair")
        print("2. Encrypt/Decrypt Message")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            private_key = generate_rsa_key_pair()
            public_key = private_key.public_key()
            private_key_filename, public_key_filename = save_rsa_keys(private_key, public_key)
            print(f"RSA key pair generated and saved.")
            print(f"Private Key: {private_key_filename}")
            print(f"Public Key: {public_key_filename}")

        elif choice == '2':
            private_key_filename = input("Enter the filename of your private key: ")
            public_key_filename = input("Enter the filename of the recipient's public key: ")

            private_key = load_rsa_private_key(private_key_filename)
            public_key = load_rsa_public_key(public_key_filename)

            message = input("Enter a message to encrypt: ").encode('utf-8')
            ciphertext = encrypt_message(public_key, message)
            print("Encrypted message:", ciphertext)

            decrypted_message = decrypt_message(private_key, ciphertext)
            print("Decrypted message:", decrypted_message.decode('utf-8'))

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
