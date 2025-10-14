# CANNOT PARSE CODE SNIPPET
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit. This basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    oranges and apples and an integer that represents the total number of fruits 
    in the basket, return the number of mango fruits in the basket.
    """
    # Split the string into a list of words
    words = s.split()

    # Loop through the list of words to find the numbers of apples and oranges
    num_apples = 0
    num_oranges = 0
    for i in range(len(words)):
        if words[i] == "apples":
            num_apples = int(words[i-1])
        elif words[i] == "oranges":
            num_oranges = int(words[i-1])

    # Calculate the number of mango fruits in the basket
    num_mangoes = n - num_apples - num_oranges
    
    return num_mangoes
