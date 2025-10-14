def by_length(arr):
    names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    sorted_arr = sorted(filter(lambda x: 1 <= x <= 9, arr))
    reversed_arr = sorted_arr[::-1]
    return [names[num] for num in reversed_arr]
