def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.split(",")
    else:
        lowercase_letters = [c for c in txt if c.islower()]
        odd_order_letters = [c for c in lowercase_letters if ord(c) % 2 == 1]
        return len(odd_order_letters)
