def by_length(arr):
    # Create a dictionary to map integers to their corresponding names
    names = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    
    # Filter out any numbers that are not between 1 and 9
    arr = [x for x in arr if x in range(1, 10)]
    
    # Sort the array in ascending order
    arr.sort()
    
    # Reverse the array
    arr.reverse()
    
    # Map each integer to its corresponding name using the names dictionary
    result = [names[x] for x in arr]
    
    return result
