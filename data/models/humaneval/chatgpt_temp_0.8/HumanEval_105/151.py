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
    # create a list of the names of the digits from one to nine
    digit_names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    
    # create a list to store the valid digits in the array
    valid_digits = []
    
    # loop through the array and add any digit between 1 and 9 to the valid_digits list
    for num in arr:
        if 1 <= num <= 9:
            valid_digits.append(num)
    
    # sort the valid digits in ascending order
    valid_digits.sort()
    
    # reverse the sorted valid digits
    valid_digits.reverse()
    
    # create a list of the digit names corresponding to the reversed valid digits
    digit_names_reversed = [digit_names[num] for num in valid_digits]
    
    # return the list of digit names
    return digit_names_reversed
