def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0

    # Converting the number to a positive integer if negative
    num = abs(num)

    # Looping through each digit of the number
    while num > 0:
        digit = num % 10
        
        # Checking if the digit is even or odd
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        # Removing the last digit from the number
        num //= 10

    return (even_count, odd_count)
