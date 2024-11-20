def karatsuba(x, y):
    # Base case for recursion: if the number is less than 10, return the product.
    if x < 10 or y < 10:
        return x * y

    # Determine the size of the numbers
    n = max(len(str(x)), len(str(y)))
    half = n // 2

    # Split the numbers into two halves
    high_x, low_x = divmod(x, 10**half)
    high_y, low_y = divmod(y, 10**half)

    # 3 recursive calls to calculate the three products
    z0 = karatsuba(low_x, low_y)            # low * low
    z1 = karatsuba(low_x + high_x, low_y + high_y)  # (low + high) * (low + high)
    z2 = karatsuba(high_x, high_y)          # high * high

    # The Karatsuba formula: z2 * 10^(2 * half) + (z1 - z2 - z0) * 10^half + z0
    return z2 * 10**(2 * half) + (z1 - z2 - z0) * 10**half + z0

def compute_square(number):
    # We are squaring the number using Karatsuba multiplication
    return karatsuba(number, number)

if __name__ == "__main__":
    # Input the large 20-digit number
    num = int(input("Enter a 20-digit number: "))
    
    # Ensure the number has exactly 20 digits
    if len(str(num)) != 20:
        print("Please enter exactly a 20-digit number.")
    else:
        # Compute the square of the number
        result = compute_square(num)
        
        # Output the result
        print(f"The square of the number is: {result}")

