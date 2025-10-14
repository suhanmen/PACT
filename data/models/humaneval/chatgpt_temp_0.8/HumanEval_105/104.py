def by_length(arr):
    # Create a dictionary to map digits to their corresponding names
    digit_names = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    
    # Filter out any values in the input array that are not between 1 and 9 inclusive
    filtered_arr = [x for x in arr if 1 <= x <= 9]
    
    # Sort the remaining values in ascending order
    sorted_arr = sorted(filtered_arr)
    
    # Reverse the sorted array
    reversed_arr = sorted_arr[::-1]
    
    # Map each digit to its corresponding name using the dictionary
    result = [digit_names[x] for x in reversed_arr]
    
    return result
