def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    # First, filter out numbers that are not between 1 and 9
    filtered = list(filter(lambda x: 1 <= x <= 9, arr))
    
    # If the filtered list is empty, return an empty list
    if not filtered:
        return []
    
    # Sort the filtered list
    sorted_list = sorted(filtered)
    
    # Reverse the sorted list
    reversed_list = sorted_list[::-1]
    
    # Convert each number to its corresponding name from the list of names
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = [names[x-1] for x in reversed_list]
    
    return result
