# CANNOT PARSE CODE SNIPPET
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for example:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    fruits = s.split()  # split the string into a list of words
    apples = 0
    oranges = 0
    for fruit in fruits:
        if fruit == "apples" or fruit == "apple":
            apples = int(fruits[fruits.index(fruit) - 1])  # get the number of apples from the previous word
        elif fruit == "oranges" or fruit == "orange":
            oranges = int(fruits[fruits.index(fruit) - 1])  # get the number of oranges from the previous word
    mangoes = n - apples - oranges  # calculate the number of mangoes
    return mangoes
