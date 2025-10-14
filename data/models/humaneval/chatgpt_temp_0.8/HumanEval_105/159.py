def by_length(arr):
    digit_names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = []
    
    # filter the array to only include integers between 1 and 9 inclusive
    filtered_arr = list(filter(lambda x: 1 <= x <= 9, arr))
    
    # sort the filtered array in ascending order
    sorted_arr = sorted(filtered_arr)
    
    # reverse the sorted array
    reversed_arr = list(reversed(sorted_arr))
    
    # replace each digit by its corresponding name
    for num in reversed_arr:
        result.append(digit_names[num])
    
    return result
