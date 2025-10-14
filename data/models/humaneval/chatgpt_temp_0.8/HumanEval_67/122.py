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
    # Split the string into a list
    lst = s.split()
    # Initialize variables to count the number of apples and oranges
    apples = 0
    oranges = 0
    # Loop through the list
    for i in range(len(lst)):
        # If the element is "apples", add the next element (which should be a number) to the apples count
        if lst[i] == "apples":
            apples += int(lst[i+1])
        # If the element is "oranges", add the next element (which should be a number) to the oranges count
        elif lst[i] == "oranges":
            oranges += int(lst[i+1])
    # Subtract the total number of apples and oranges from the total number of fruits to get the number of mangoes
    mangoes = n - apples - oranges
    return mangoes
