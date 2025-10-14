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

    # Filter out strange numbers (not between 1 and 9) from the array
    filtered_arr = [num for num in arr if 1 <= num <= 9]

    # If the filtered array is empty, return an empty array
    if not filtered_arr:
        return []

    # Sort the filtered array
    sorted_arr = sorted(filtered_arr)

    # Reverse the sorted array
    reversed_arr = sorted_arr[::-1]

    # Map each integer to its corresponding name using the dictionary
    result = [num_to_name[num] for num in reversed_arr]

    return result
