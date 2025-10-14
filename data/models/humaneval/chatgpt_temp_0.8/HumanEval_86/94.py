def anti_shuffle(s):
    words = s.split(" ") # split the string into words
    new_words = []
    for word in words:
        sorted_word = "".join(sorted(word)) # sort the characters in each word
        new_words.append(sorted_word)
    return " ".join(new_words) # join the words back together with spaces
