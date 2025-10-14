def by_length(arr):
    names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = []
    for num in arr:
        if 1 <= num <= 9:
            result.append(num)
    result.sort(reverse=True)
    result = [names[num] for num in result]
    return result
