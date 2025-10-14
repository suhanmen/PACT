def by_length(arr):
    name_dict = {
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
    
    # Filter out strange numbers and sort the remaining numbers
    arr = sorted([num for num in arr if 1 <= num <= 9])
    
    # Reverse the array and convert each digit to its corresponding name
    return [name_dict[num] for num in arr[::-1]]
