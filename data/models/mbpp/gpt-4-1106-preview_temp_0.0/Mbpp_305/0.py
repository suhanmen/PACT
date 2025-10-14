"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""



def start_withp(word_list):
    # Initialize an empty list to store words starting with 'p'
    p_words = []

    # Iterate over each string in the word_list
    for words in word_list:
        # Split the string into individual words
        split_words = words.split()

        # Iterate over each word in the split words
        for word in split_words:
            # Check if the word starts with 'p' or 'P'
            if word.lower().startswith('p'):
                # Append the word to the p_words list
                p_words.append(word)

    # Return the first two words that start with 'p'
    # If there are less than two words, it will return as many as are available
    return tuple(p_words[:2])

# Example usage
# assert start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')
