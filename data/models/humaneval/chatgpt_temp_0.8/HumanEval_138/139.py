def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is even and greater than or equal to 8
    if n >= 8 and n % 2 == 0:
        # Set a counter to keep track of the number of even numbers found
        count = 0
        # Loop through even numbers up to half of n
        for i in range(2, n//2 + 1, 2):
            # Check if the remainder of n - i is even
            if (n - i) % 2 == 0:
                # Increment the counter
                count += 1
                # Check if 4 even numbers have been found
                if count == 4:
                    return True
        # If no 4 even numbers are found
        return False
    # If n is not even and greater than or equal to 8
    else:
        return False
