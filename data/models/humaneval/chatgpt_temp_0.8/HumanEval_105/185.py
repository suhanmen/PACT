def by_length(arr):
    # Create a dictionary to map integers to their corresponding names
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

    # Create a list to hold the sorted and filtered integers
    filtered_integers = []

    # Iterate through the input array and add any integers between 1 and 9 to filtered_integers
    for num in arr:
        if num >= 1 and num <= 9:
            filtered_integers.append(num)

    # Sort the filtered integers in ascending order
    filtered_integers.sort()

    # Reverse the sorted integers
    filtered_integers.reverse()

    # Create a list to hold the corresponding names for the integers
    digit_names_list = []

    # Iterate through the filtered integers and add their corresponding names to digit_names_list
    for num in filtered_integers:
        digit_names_list.append(digit_names[num])

    # Return digit_na
