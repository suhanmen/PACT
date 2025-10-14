def split_words(txt):
    # Check if whitespace exists
    if " " in txt:
        return txt.split()
    # Check if comma exists
    elif "," in txt:
        return txt.split(",")
    else:
        # Count the number of lower-case letters with odd order in the alphabet
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 != 0:
                count += 1
        return count
