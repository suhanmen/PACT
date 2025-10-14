def by_length(arr):
    # create a list of names for digits
    names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    # filter out any strange numbers
    arr = list(filter(lambda x: 1 <= x <= 9, arr))
    # sort the array
    arr.sort()
    # reverse the array
    arr = arr[::-1]
    # convert digits to their corresponding names
    result = [names[i] for i in arr]
    return result
