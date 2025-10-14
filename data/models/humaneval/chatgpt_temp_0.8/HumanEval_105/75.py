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
    valid_nums = []
    for num in arr:
        if num >= 1 and num <= 9:
            valid_nums.append(num)
    sorted_nums = sorted(valid_nums)
    reversed_nums = list(reversed(sorted_nums))
    word_nums = []
    for num in reversed_nums:
        if num == 1:
            word_nums.append("One")
        elif num == 2:
            word_nums.append("Two")
        elif num == 3:
            word_nums.append("Three")
        elif num == 4:
            word_nums.append("Four")
        elif num == 5:
            word_nums.append("Five")
        elif num == 6:
            word_nums.append("Six")
        elif num == 7:
            word_nums.append("Seven")
        elif num == 8:
            word_nums.append("Eight")
        elif num == 9:
            word_nums.append("Nine")
    return word_nums
