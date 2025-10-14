def pluck(arr):
    evens = [x for x in arr if x % 2 == 0]
    if not evens:
        return []
    else:
        smallest_even = min(evens)
        index = arr.index(smallest_even)
        return [smallest_even, index]
