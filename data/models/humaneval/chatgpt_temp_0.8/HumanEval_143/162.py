def is_prime(num):
    """
    Helper function to check whether a number is prime or not.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Returns a string that contains the words from the original sentence,
    whose lengths are prime numbers.
    """
    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)
