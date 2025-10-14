def by_length(arr):
    digit_names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    filtered_arr = [num for num in arr if 1 <= num <= 9] # filter out numbers outside the range of 1-9
    sorted_arr = sorted(filtered_arr)
    reversed_arr = list(reversed(sorted_arr))
    result_arr = []
    for num in reversed_arr:
        result_arr.append(digit_names[num])
    return result_arr
