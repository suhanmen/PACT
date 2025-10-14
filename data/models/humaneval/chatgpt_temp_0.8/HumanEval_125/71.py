def split_words(txt):
    # If there are whitespaces in the text, split on them and return the list
    if ' ' in txt:
        return txt.split()
    # If there are no whitespaces but commas, split on commas and return the list
    elif ',' in txt:
        return txt.split(',')
    # If there are neither whitespaces nor commas, count the number of lower-case letters with odd order in 
    # the alphabet and return the count
    else:
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 == 1:
                count += 1
        return count
