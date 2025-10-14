def by_length(arr):
    digit_names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    filtered_arr = [x for x in arr if 1 <= x <= 9]
    filtered_arr.sort()
    filtered_arr.reverse()
    result_arr = [digit_names[x] for x in filtered_arr]
    return result_arr
