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
    nums = [num for num in arr if 1 <= num <= 9] # filter out numbers not between 1 and 9
    nums = sorted(nums) # sort the numbers
    nums = nums[::-1] # reverse the numbers
    words = []
    for num in nums:
        if num == 1:
            words.append("One")
        elif num == 2:
            words.append("Two")
        elif num == 3:
            words.append("Three")
        elif num == 4:
            words.append("Four")
        elif num == 5:
            words.append("Five")
        elif num == 6:
            words.append("Six")
        elif num == 7:
            words.append("Seven")
        elif num == 8:
            words.append("Eight")
        elif num == 9:
            words.append("Nine")
    return words
