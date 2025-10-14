def is_prime(n):
    """
    This is a helper function that checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split()
    res = []
    for word in words:
        if is_prime(len(word)):
            res.append(word)
    return ' '.join(res)
