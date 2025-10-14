def pluck(arr):
    even_nums = [num for num in arr if num % 2 == 0]
    if not even_nums:
        return []
    else:
        min_even = min(even_nums)
        min_even_index = arr.index(min_even)
        return [min_even, min_even_index]
