def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def words_in_sentence(sentence):
    # Split sentence into a list of words
    words = sentence.split()

    # Filter out words whose length is not a prime number
    prime_words = [word for word in words if is_prime(len(word))]

    # Join the prime words into a single string
    result = " ".join(prime_words)

    return result
