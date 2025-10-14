def anti_shuffle(s):
    words = s.split(" ")
    result = ""
    for word in words:
        sorted_word = "".join(sorted(word, key=lambda x: ord(x)))
        result += sorted_word + " "
    return result[:-1]
