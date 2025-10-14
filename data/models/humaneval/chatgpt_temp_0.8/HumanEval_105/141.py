def by_length(arr):
    # Define a dictionary to map digits to their corresponding names
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

    # Filter out numbers that are not between 1 and 9 inclusive
    arr = [num for num in arr if num in range(1, 10)]

    # Sort the resulting array
    arr.sort()

    # Reverse the resulting array
    arr.reverse()

    # Map each digit to its corresponding name
    names = [digit_names[num] for num in arr]

    return names
