def by_length(arr):
    digit_names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    sorted_arr = sorted([x for x in arr if 1 <= x <= 9])
    reversed_arr = sorted_arr[::-1]
    result = [digit_names[x] for x in reversed_arr]
    return result
