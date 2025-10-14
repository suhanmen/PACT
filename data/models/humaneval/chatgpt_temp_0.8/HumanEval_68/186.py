python
def pluck(arr):
    even_nums = [n for n in arr if n % 2 == 0]
    if not even_nums:
        return []
    else:
        smallest_even = min(even_nums)
        smallest_index = arr.index(smallest_even)
        return [smallest_even, smallest_index]
