from collections import Counter

def find_max(words):
    # Get the list of unique characters for each word
    unique_chars = [set(word) for word in words]
    # Count the number of unique characters for each word
    counts = [len(chars) for chars in unique_chars]
    # Find the maximum count
    max_count = max(counts)
    # Get the indices of all words with the maximum count
    max_indices = [i for i, count in enumerate(counts) if count == max_count]
    # If there is only one word with the maximum count, return it
    if len(max_indices) == 1:
        return words[max_indices[0]]
    else:
        # Sort the indices by lexicographical order
        sorted_indices = sorted(max_indices, key=lambda i: words[i])
        # Return the word with the first index in sorted_indices
        return words[sorted_indices[0]]
