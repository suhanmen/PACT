def anti_shuffle(s):
    # Split the string into individual words
    words = s.split()

    # Convert each word to its ordered version and store in a list
    new_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))
        new_words.append(ordered_word)

    # Combine the ordered words into a string, keeping the original order of words and spaces
    result = ''
    for i in range(len(words)):
        result += new_words[i]
        # Add the space back in unless this is the last word
        if i < len(words) - 1:
            result += ' '
    
    return result
