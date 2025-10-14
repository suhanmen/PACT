def words_in_sentence(sentence):
    # Define a helper function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Split the sentence into words
    words = sentence.split()
    
    # Filter the words whose lengths are prime numbers
    prime_words = [word for word in words if is_prime(len(word))]
    
    # Join the prime words into a new sentence
    new_sentence = ' '.join(prime_words)
    
    return new_sentence
