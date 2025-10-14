def by_length(arr):
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    # Filter out strange numbers
    arr = [n for n in arr if 1 <= n <= 9]
    # Sort and reverse the array
    arr = sorted(arr, reverse=True)
    # Convert integers to corresponding names
    arr = [names[n-1] for n in arr]
    return arr
