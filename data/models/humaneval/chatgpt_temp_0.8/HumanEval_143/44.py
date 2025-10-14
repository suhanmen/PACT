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
    # Define a helper function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    # Split the sentence into words
    words = sentence.split()

    # Create a list to store the words whose lengths are prime numbers
    prime_words = []

    # Loop through the words and check if their lengths are prime numbers
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    # Join the prime words with a space and return the result
    return ' '.join(prime_words)
