def even_odd_count(num):
    even_count = 0
    odd_count = 0

    # Convert number to string to easily extract digits
    num_str = str(num)

    # Iterate over all digits in the number
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)
