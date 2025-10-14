def words_in_sentence(sentence):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**(1/2))+1):
            if n%i == 0:
                return False
        return True

    result = []
    for word in sentence.split():
        if is_prime(len(word)):
            result.append(word)
    
    return " ".join(result)
