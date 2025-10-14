def select_words(s, n):
    vowels = "aeiouAEIOU"
    words = s.split()
    result = []
    for word in words:
        cons_count = sum(1 for letter in word if letter not in vowels)
        if cons_count == n:
            result.append(word)
    return result
