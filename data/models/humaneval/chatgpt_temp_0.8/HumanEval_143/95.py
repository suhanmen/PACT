def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    primes = []
    words = sentence.split()
    for word in words:
        if is_prime(len(word)):
            primes.append(word)
    return " ".join(primes)
