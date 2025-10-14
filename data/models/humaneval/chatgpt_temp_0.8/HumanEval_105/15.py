def by_length(arr):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = [num for num in arr if num in nums]
    arr.sort()
    arr.reverse()
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [names[num-1] for num in arr]
