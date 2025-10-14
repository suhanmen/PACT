def count_nums(arr):
    def get_signed_digits(n):
        digits = [int(d) for d in str(n) if d.isdigit()]
        if n < 0:
            digits[0] = -digits[0]
        return digits

    count = 0
    for num in arr:
        if sum(get_signed_digits(num)) > 0:
            count += 1
    return count
