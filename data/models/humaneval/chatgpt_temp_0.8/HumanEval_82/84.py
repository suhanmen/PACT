def prime_length(string):
    length = len(string)
    if length == 1:
        return False
    elif length == 2:
        return True
    else:
        for i in range(2, int(length/2)+1):
            if length % i == 0:
                return False
        return True
