def unique_digits(x):
    result = []
    for num in x:
        if all(int(i) % 2 != 0 for i in str(num)):
            result.append(num)
    return sorted(result)
