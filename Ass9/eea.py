# 13mod5-=>2
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def modular_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd == 1:
        return x % m
    else:
        return None

# Example usage:
a = int(input("Enter the value of a: "))
m = int(input("Enter the value of m: "))

result = modular_inverse(a, m)

if result is not None:
    print(f"The modular inverse of {a} modulo {m} is: {result}")
else:
    print(f"The modular inverse does not exist for {a} modulo {m}.")
