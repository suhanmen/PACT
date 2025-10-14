def by_length(arr):
    num_names = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    # Create a dictionary that maps integers to their corresponding names

    arr = [num for num in arr if 1 <= num <= 9]
    # Filter out any integers that are not between 1 and 9

    arr.sort()
    arr.reverse()
    # Sort the array and reverse it

    result = [num_names[num] for num in arr]
    # Replace each integer by its corresponding name

    return result
