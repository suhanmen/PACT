def select_words(s, n):
    if not s:
        return []
    
    def count_consonants(word):
        consonants = set("bcdfghjklmnpqrstvwxyz")
        return sum(1 for c in word.lower() if c in consonants)
    
    words = s.split()
    return [w for w in words if count_consonants(w) == n]
