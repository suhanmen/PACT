def pluck(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    if len(even_numbers) == 0:
        return []
    else:
        smallest_even = min(even_numbers)
        smallest_even_index = arr.index(smallest_even)
        return [smallest_even, smallest_even_index]
