from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii

def encrypt_AES_GCM(plaintext, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return cipher.nonce, ciphertext, tag

def decrypt_AES_GCM(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext
    except ValueError:
        return None

# Generate a 256-bit random encryption key
secretKey = get_random_bytes(32)
print("Encryption key:", binascii.hexlify(secretKey).decode('utf-8'))

msg = input("Enter msg for Encryption: ").encode("utf-8")

nonce, ciphertext, tag = encrypt_AES_GCM(msg, secretKey)

print("encryptedMsg", {
    "ciphertext": binascii.hexlify(ciphertext).decode('utf-8'),
    # "nonce": binascii.hexlify(nonce).decode('utf-8'),
    # "authTag": binascii.hexlify(tag).decode('utf-8')
})

decryptedMsg = decrypt_AES_GCM(nonce, ciphertext, tag, secretKey)

if decryptedMsg is not None:
    print("decryptedMsg:", decryptedMsg.decode('utf-8'))
else:
    print("Decryption failed. The message may have been tampered with.")
