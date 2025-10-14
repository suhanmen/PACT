def int_to_mini_roman(number):
    if not 1 <= number <= 1000:
        raise ValueError("number must be between 1 and 1000")
    roman_nums = ("m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i")
    arabic_nums = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    result = ""
    for r, a in zip(roman_nums, arabic_nums):
        count = number // a
        result += r * count
        number -= a * count
    return result.lower()
