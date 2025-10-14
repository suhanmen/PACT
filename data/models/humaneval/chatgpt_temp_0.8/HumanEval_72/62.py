def will_it_fly(q,w):
    if q != q[::-1]:
        return False
    elif sum(q) > w:
        return False
    else:
        return True
