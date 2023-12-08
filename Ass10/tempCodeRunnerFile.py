def extended_gcd(a, b):
    """Computes the greatest common divisor of two integers a and b, and
    also computes the Bezout coefficients, x and y, such that the following equation holds:
    
    ax + by = gcd(a, b)
    """
    
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y   

def modular_inverse(a, m):
    """Computes the modular inverse of a modulo m.

    Args:
      a: An integer.
      m: An integer.

    Returns:
      The modular inverse of a modulo m, or None if no modular inverse exists.
    """

    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def chinese_remainder_theorem(a, m):
    """Solves the system of linear congruences x ≡ a[i] (mod m[i]) using the CRT.

    Args:
      a: A list of integers.
      m: A list of pairwise coprime integers.

    Returns:
      An integer x that satisfies all of the congruences.
    """

    # Check that the lengths of a and m are the same.
    assert len(a) == len(m)

    # Calculate the product of all moduli.
    M = 1
    for mi in m:
        M *= mi

    # Calculate x using the CRT.
    x = 0
    for i in range(len(a)):
        mi = m[i]
        Mi = M // mi
        xi = modular_inverse(Mi, mi)
        x += a[i] * Mi * xi

    return x % M

def get_input():
    a = []
    m = []

    n = int(input("Enter the number of congruences: "))
    for i in range(n):
        ai = int(input(f"Enter a[{i}]: "))
        mi = int(input(f"Enter m[{i}]: "))
        a.append(ai)
        m.append(mi)

    return a, m

def main():
    a, m = get_input()
    x = chinese_remainder_theorem(a, m)
    print("Solution x:", x)

if __name__ == "__main__":
    main()
