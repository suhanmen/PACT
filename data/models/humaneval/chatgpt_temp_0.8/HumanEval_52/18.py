def below_threshold(l: list, t: int):
    for num in l:
        if num >= t:
            return False
    return True
