def histogram(test):
    letter_count = {}
    highest_count = 0
    for letter in test.split():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
        if letter_count[letter] > highest_count:
            highest_count = letter_count[letter]
    result = {}
    for letter in letter_count:
        if letter_count[letter] == highest_count:
            result[letter] = highest_count
    return result
