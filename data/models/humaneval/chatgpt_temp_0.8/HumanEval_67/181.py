# CANNOT PARSE CODE SNIPPET
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit. This basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represents the total number of the fruits 
    in the basket, return the number of the mango fruits in the basket.
    """
    # Split the input string into separate words
    words = s.split()
    
    # Find the number of apples and oranges in the basket
    apples = int(words[0])
    oranges = int(words[3])
    
    # Calculate the number of mangoes in the basket
    mangoes = n - apples - oranges
    
    return mangoes
