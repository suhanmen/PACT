def words_in_sentence(sentence):
    def is_prime(num):
        """
        Helper function to check if a number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = ""
    words = sentence.split()
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()
