def even_odd_count(num):
    even_count = 0
    odd_count = 0

    # Convert the integer to a string to iterate through each digit
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # If the original number was negative, subtract the odd and even counts
    if num < 0:
        odd_count *= -1
        even_count *= -1

    return even_count, odd_count
