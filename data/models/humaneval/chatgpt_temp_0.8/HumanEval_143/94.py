def words_in_sentence(sentence):
    # define a function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # split the sentence into words
    words = sentence.split()
    # initialize an empty list to store the words with prime length
    prime_words = []
    for word in words:
        # check if the length of the word is prime
        if is_prime(len(word)):
            prime_words.append(word)
    # join the prime words with a space separator and return the result
    return ' '.join(prime_words)
