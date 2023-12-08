# from Crypto.Cipher import DES
from Crypto.Cipher import DES

from secrets import token_bytes


key = token_bytes(8)


def encrypt(msg):
    cipher = DES.new(key,DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext,tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    # print(f'cipher text Text is-=>: {ciphertext}')
    return nonce, ciphertext,tag


def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)


    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False


print('\n*** Data Encryption Standard Algorithm ***')
nonce, ciphertext, tag = encrypt(input('Enter Plain Text:'))
plaintext = decrypt(nonce,ciphertext,tag)


print(f'Cipher Text is: {ciphertext}')


if not plaintext:
    print('Message is Corrupted!')
else:
    print(f'Plain Text is: {plaintext}')