def histogram(test):
    """
    Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    """
    if not test:
        return {}
    
    # split the string into a list
    lst = test.split()
    
    # create an empty dictionary to store the count of each letter
    count_dict = {}
    
    # iterate through the list and update the count of each letter
    for letter in lst:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    
    # find the maximum count of any letter
    max_count = max(count_dict.values())
    
    # create a list of letters that have the maximum count
    max_letters = [k for k, v in count_dict.items() if v == max_count]
    
    # create a dictionary containing the max letters and their corresponding counts
    result = {letter: coun
