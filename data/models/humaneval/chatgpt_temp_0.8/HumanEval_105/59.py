def by_length(arr):
    digit_names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    # Filter out strange numbers and sort the remaining ones
    filtered_arr = sorted(filter(lambda x: 1 <= x <= 9, arr))
    
    # Reverse the filtered array and map the digits to their names
    return list(map(lambda x: digit_names[x], filtered_arr[::-1]))
