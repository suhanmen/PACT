def is_prime(num):
    """
    Helper function that returns True if the given number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Given a string representing a sentence, returns a string that contains the words from the original sentence
    whose lengths are prime numbers. The order of the words in the new string should be the same as the original one.
    """
    result = []
    for word in sentence.split():
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)
