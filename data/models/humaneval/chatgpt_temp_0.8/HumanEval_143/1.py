def words_in_sentence(sentence):
    def is_prime(n):
        """
        This function checks whether the given number is prime or not.
        """
        if n < 2:
            return False
        for i in range(2, int(n**(0.5))+1):
            if n % i == 0:
                return False
        return True

    # Split the sentence into words and filter out the words whose lengths are prime numbers.
    words = filter(lambda word: is_prime(len(word)), sentence.split())

    # Join the filtered words using space as a separator.
    return ' '.join(words)
