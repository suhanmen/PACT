def by_length(arr):
    # Define a dictionary to store number names
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
    
    # Filter out numbers that are not between 1 and 9
    arr = [num for num in arr if 1 <= num <= 9]
    
    # Sort the array
    arr.sort()
    
    # Reverse the array
    arr.reverse()
    
    # Replace each digit by its corresponding name
    arr = [names[num] for num in arr]
    
    return arr
