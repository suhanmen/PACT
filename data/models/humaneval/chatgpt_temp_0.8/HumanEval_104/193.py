def unique_digits(x):
    def has_even_digit(num):
        while num > 0:
            if num % 2 == 0:
                return True
            num = num // 10
        return False
    
    result = []
    for num in x:
        if not has_even_digit(num):
            result.append(num)
    
    return sorted(result)
