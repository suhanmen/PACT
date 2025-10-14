def by_length(arr):
    digit_names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    
    if not filtered_arr:
        return []
    
    filtered_arr.sort()
    filtered_arr.reverse()
    
    result = [digit_names[num] for num in filtered_arr]
    return result
