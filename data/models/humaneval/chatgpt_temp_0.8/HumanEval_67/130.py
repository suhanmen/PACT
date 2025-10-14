# CANNOT PARSE CODE SNIPPET
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    # split the string into a list of words
    words = s.split()
    
    # initialize counts for apples and oranges to 0
    apples = 0
    oranges = 0
    
    # loop through the words and count the number of apples and oranges
    for word in words:
        if word == 'apples':
            apples = int(words[words.index(word) - 1])
        elif word == 'oranges':
            oranges = int(words[words.index(word) - 1])
    
    # subtract the number of apples and oranges from the total number of fruits
    mangoes = n - apples - oranges
    
    # return the number of mangoes
    return mangoes
