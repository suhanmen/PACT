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
    
    # Filter out any strange numbers
    arr = [num for num in arr if 1 <= num <= 9]
    
    # Sort and reverse the array
    arr.sort()
    arr.reverse()
    
    # Replace integers with their corresponding names
    result = [num_to_name[num] for num in arr]
    
    return result
