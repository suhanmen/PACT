def words_in_sentence(sentence):
    # function to check if a number is prime or not
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    # split the sentence into words
    words = sentence.split()
    
    # filter out words whose length is a prime number
    prime_words = filter(lambda x: is_prime(len(x)), words)
    
    # join the prime words into a sentence
    result = " ".join(prime_words)
    
    return result
