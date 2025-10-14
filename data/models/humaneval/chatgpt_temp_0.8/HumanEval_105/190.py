def by_length(arr):
    # Create a dictionary to map integers to their corresponding names
    num_to_name = {
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
    
    # Filter out any numbers that are outside the range 1-9
    arr = [x for x in arr if 1 <= x <= 9]
    
    # Sort the filtered array
    arr.sort()
    
    # Reverse the sorted array
    arr.reverse()
    
    # Map each integer to its corresponding name using the dictionary, and return the resulting list
    return [num_to_name[x] for x in arr]
