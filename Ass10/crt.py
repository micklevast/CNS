import math
# num[] = {3, 4, 5}, rem[] = {2, 3, 1}-=>x=11
# num[] = {5, 7}, rem[] = {1, 3}-=>x=31
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y   

def modular_inverse(a, m):
    # Calculate the modular inverse using Fermat's Little Theorem
    return pow(a, -1, m)

def chinese_remainder_theorem(num, rem):
    assert len(num) == len(rem)

    # Calculate the product of all moduli.
    M = math.prod(num)

    # Calculate x using the CRT.
    x = 0
    for i in range(len(num)):
        ai = rem[i]
        mi = num[i]
        Mi = M // mi
        xi = modular_inverse(Mi, mi)
        if xi is None:
            print("Modular inverse does not exist. CRT cannot be applied.")
            return None
        x += ai * Mi * xi

    return x % M

def get_input():
    num = []
    rem = []

    n = int(input("Enter the number of congruences: "))

    # Input for num
    print("Enter values for num:")
    for i in range(n):
        num_i = int(input(f"Enter num[{i}]: "))
        num.append(num_i)

    # Input for rem
    print("Enter values for rem:")
    for i in range(n):
        rem_i = int(input(f"Enter rem[{i}]: "))
        rem.append(rem_i)

    return num, rem

def main():
    num, rem = get_input()

    # Calculate CRT
    result = chinese_remainder_theorem(num, rem)
    if result is not None:
        print("Smallest number:", result)

if __name__ == "__main__":
    main()


## ----------------------------------------
# The Chinese Remainder Theorem (CRT) is a mathematical concept that provides a solution to a system of simultaneous modular congruences.
# The theorem is particularly useful in number theory and modular arithmetic. The CRT states that if you have a set of equations of the form:


# In summary, the Chinese Remainder Theorem function efficiently combines individual modular congruences to find a unique solution for 
# x modulo the product of the moduli. This theorem has applications in various areas, including cryptography, error detection and correction, and number theory.