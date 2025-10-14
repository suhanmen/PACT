def split_words(txt):
    if " " in txt:
        # If whitespace exists, split on whitespace
        return txt.split()
    elif "," in txt:
        # If no whitespace but commas exist, split on commas
        return txt.split(",")
    else:
        # If neither whitespace nor commas exist, count lower-case letters with odd order in the alphabet
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 == 1:
                count += 1
        return count
