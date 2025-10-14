def unique_digits(x):
    result = []
    for num in x:
        if not any(int(digit) % 2 == 0 for digit in str(num)):
            result.append(num)
    return sorted(result)
