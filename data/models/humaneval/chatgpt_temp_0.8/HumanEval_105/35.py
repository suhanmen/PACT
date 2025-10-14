def by_length(arr):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    filtered_arr = [n for n in arr if n in nums]
    if not filtered_arr:
        return []
    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]
    digit_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [digit_names[n-1] for n in reversed_arr]
