def by_length(arr):
    num_names = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    
    # remove any strange numbers from the array
    arr = [x for x in arr if 1 <= x <= 9]
    
    # sort the array and reverse it
    arr.sort(reverse=True)
    
    # replace each integer with its corresponding name
    result = [num_names[x] for x in arr]
    
    return result
