def words_in_sentence(sentence):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    result = []
    words = sentence.split()
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)
