def is_prime(n):
    """
    Helper function to check if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    # Split the sentence into words
    words = sentence.split()
    # Initialize an empty list to store prime words
    prime_words = []
    # Iterate over the words
    for word in words:
        # Check if the length of the word is prime
        if is_prime(len(word)):
            # Append the word to the list of prime words
            prime_words.append(word)
    # Join the prime words int
