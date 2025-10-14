def by_length(arr):
    num_names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    filtered_arr = [num for num in arr if 1 <= num <= 9] # filter out strange numbers
    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]
    result = [num_names[num] for num in reversed_arr]
    return result
