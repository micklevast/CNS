def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean(b, a % b)
        return gcd, y, x - (a // b) * y

while True:
    try:
        a = int(input("Enter the first integer (a): "))
        b = int(input("Enter the second integer (b): "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        continue

    gcd, x, y = extended_euclidean(a, b)
    print(f"GCD of {a} and {b} is {gcd}")
    print(f"x = {x}, y = {y}")

    another = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if another != "yes":
        break


## ============================
