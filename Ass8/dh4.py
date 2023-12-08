import random

def is_primitive_root(g, p):
    # Check if g is a primitive root of p
    if g == 1:
        return False

    distinct_powers = set()


    for j in range(1, p):
        distinct_powers.add(pow(i, j, p))
        if len(distinct_powers) == p - 1:
            return True

    return False

        
    

def generate_primitive_root(p):
    # Generate a primitive root g for the prime number p
    g=1;
    distinct_powers = set()

    for i in range(1, p):
        for j in range(1, p):
            distinct_powers.add(pow(i, j, p))
            if len(distinct_powers) == p - 1:
                return i
        distinct_powers.clear()
    return -1;

# Get the prime number p from the user
p = int(input("Enter a prime number (p): "))

# Generate a primitive root g for p
g = generate_primitive_root(p)

if g is None:
    print("No primitive root found for the given prime number. Please choose a different prime number.")
else:
    print(f"Primitive root (g) for p={p}: {g}")

    # Alice's private key
    a = random.randint(1, p - 1)

    # Bob's private key
    b = random.randint(1, p - 1)

    # Calculate Alice's public key
    Y_A = pow(g, a, p)

    # Calculate Bob's public key
    Y_B = pow(g, b, p)

    # Exchange public keys (normally done over an insecure channel)
    print("Shared parameters:")
    print(f"p: {p}")
    print(f"g: {g}")
    print()

    print("Alice's parameters:")
    print(f"Private key (a): {a}")
    print(f"Public key (Y_A): {Y_A}")
    print()

    print("Bob's parameters:")
    print(f"Private key (b): {b}")
    print(f"Public key (Y_B): {Y_B}")
    print()

    # Calculate the shared secret key for Alice
    K_A = pow(Y_B, a, p)

    # Calculate the shared secret key for Bob
    K_B = pow(Y_A, b, p)

    print("Shared secret keys:")
    print(f"K_A: {K_A}")
    print(f"K_B: {K_B}")
    print()

    # Both Alice and Bob should have the same shared secret key
    assert K_A == K_B

    print(f"Shared secret key: {K_A}")
