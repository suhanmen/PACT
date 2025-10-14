def unique_digits(x):
    result = []
    for num in x:
        has_even_digit = False
        for digit in str(num):
            if int(digit) % 2 == 0:
                has_even_digit = True
                break
        if not has_even_digit:
            result.append(num)
    return sorted(result)
