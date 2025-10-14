def find_max(words):
    unique_counts = {}
    for word in words:
        unique_counts[word] = len(set(word))
        
    max_count = max(unique_counts.values())
    
    max_words = [key for key, value in unique_counts.items() if value == max_count]
    
    return sorted(max_words)[0]
