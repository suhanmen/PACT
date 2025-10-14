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
    # Split the string into a list of individual words
    words = s.split()
    # Initialize a variable to keep track of the number of apples and oranges
    fruit_count = 0
    # Iterate over the words and check if they represent apples or oranges
    for word in words:
        if word == "apples" or word == "oranges":
            # If the word is apples or oranges, add the preceding word (which should be a number) to the fruit count
            fruit_count += int(words[words.index(word) - 1])
    # The number of mango fruits is the total number of fruits in the basket minus the number of apples and oranges
    mango_count = n - fruit_count
    return mango_count
