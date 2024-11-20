def karatsuba(x, y):
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y

    # Number of digits in the largest number
    n = max(len(str(x)), len(str(y)))
    m = n // 2  # Half the number of digits

    # Split the digits
    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    # Recursively compute the three products
    z0 = karatsuba(b, d)  # b * d
    z2 = karatsuba(a, c)  # a * c
    z1 = karatsuba(a + b, c + d) - z2 - z0  # (a + b) * (c + d) - z2 - z0

    # Combine the results
    return (z2 * 10*(2*m)) + (z1 * 10*m) + z0

# Test case
x = 1234
y = 5678
z = karatsuba(x, y)
print("Result of", x, "x", y, "=", z)

Output: Result of 1234 x 5678 = 11052
