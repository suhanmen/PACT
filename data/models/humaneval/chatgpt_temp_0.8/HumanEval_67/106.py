def fruit_distribution(s,n):
    # Split the string into a list of words
    words = s.split()

    # Find the indices of the words "apples" and "oranges"
    apple_index = words.index("apples")
    orange_index = words.index("oranges")

    # Extract the numbers of apples and oranges from the list of words
    num_apples = int(words[apple_index - 1])
    num_oranges = int(words[orange_index - 1])

    # Calculate the number of mango fruits
    num_mangoes = n - num_apples - num_oranges

    return num_mangoes
