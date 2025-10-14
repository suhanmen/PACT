python
def words_in_sentence(sentence):
    # helper function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # split the sentence into words
    words = sentence.split()

    # filter out words whose length is not a prime number
    prime_words = filter(lambda w: is_prime(len(w)), words)

    # join the remaining words with a space and return
    return " ".join(prime_words)
