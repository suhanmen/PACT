def fruit_distribution(s,n):
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
    # First, we need to extract the number of apples and oranges from the given string
    # We can split the string by the word "and" to get separate strings for each type of fruit
    apple_str, orange_str = s.split(" and ")
    
    # Then, we can extract the number of each type of fruit using regular expressions
    # We can use the \d+ pattern to match one or more digits
    import re
    num_apples = int(re.findall("\d+", apple_str)[0])
    num_oranges = int(re.findall("\d+", orange_str)[0])
    
    # Finally, we can calculate the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits
    num_mangoes = n - num_apples - num_oranges
    
    return num_mangoes
