def by_length(arr):
    # create a dictionary to map integers to their corresponding names
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

    # filter out any strange numbers from the array
    valid_nums = [num for num in arr if 1 <= num <= 9]

    # sort the valid numbers in ascending order
    sorted_nums = sorted(valid_nums)

    # reverse the sorted numbers
    reversed_nums = sorted_nums[::-1]

    # map each number to its corresponding name
    name_arr = [digit_names[num] for num in reversed_nums]

    return name_arr
