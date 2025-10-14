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
    # First, we need to extract the number of apples and oranges from the string s
    # We can do this by splitting the string on the word "and"
    apple_str, orange_str = s.split("and")
    
    # Then, we can extract the number of apples and oranges by splitting each string on the word "apples" or "oranges"
    apples = int(apple_str.strip().split(" ")[0])
    oranges = int(orange_str.strip().split(" ")[0])
    
    # Finally, we can calculate the number of mangoes by subtracting the number of apples and oranges from the total number of fruits
    mangoes = n - apples - oranges
    
    return mangoes
