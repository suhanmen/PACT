def words_in_sentence(sentence):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    
    words = sentence.split()
    prime_length_words = []
    
    for word in words:
        if is_prime(len(word)):
            prime_length_words.append(word)
    
    return " ".join(prime_length_words)
