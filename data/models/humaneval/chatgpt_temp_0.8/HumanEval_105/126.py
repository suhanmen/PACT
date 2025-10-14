def by_length(arr):
    # Define a dictionary to map integers to their corresponding names
    names = {
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
    
    # Filter out elements that are not between 1 and 9
    arr = [x for x in arr if 1 <= x <= 9]
    
    # Sort the remaining elements and reverse the order
    arr = sorted(arr, reverse=True)
    
    # Replace each integer with its corresponding name using the dictionary
    arr = [names[x] for x in arr]
    
    return arr
