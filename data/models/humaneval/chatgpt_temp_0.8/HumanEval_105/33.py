def by_length(arr):
    # Create a mapping of numbers to their corresponding names
    num_names = {1: "One", 2: "Two", 3: "Three",
                 4: "Four", 5: "Five", 6: "Six",
                 7: "Seven", 8: "Eight", 9: "Nine"}

    # Filter out any numbers that are not between 1 and 9
    filtered_arr = [num for num in arr if num in range(1, 10)]

    # Sort the filtered array in ascending order
    sorted_arr = sorted(filtered_arr)

    # Reverse the sorted array
    reversed_arr = sorted_arr[::-1]

    # Convert each number to its corresponding name
    names_arr = [num_names[num] for num in reversed_arr]

    return names_arr
