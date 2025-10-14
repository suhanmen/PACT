def by_length(arr):
    result = []

    # sort the integers between 1 and 9 inclusive
    sorted_arr = sorted(filter(lambda x: 1 <= x <= 9, arr))

    # reverse the resulting array
    sorted_arr.reverse()

    # replace each digit by its corresponding name
    for num in sorted_arr:
        if num == 1:
            result.append("One")
        elif num == 2:
            result.append("Two")
        elif num == 3:
            result.append("Three")
        elif num == 4:
            result.append("Four")
        elif num == 5:
            result.append("Five")
        elif num == 6:
            result.append("Six")
        elif num == 7:
            result.append("Seven")
        elif num == 8:
            result.append("Eight")
        elif num == 9:
            result.append("Nine")

    return result
