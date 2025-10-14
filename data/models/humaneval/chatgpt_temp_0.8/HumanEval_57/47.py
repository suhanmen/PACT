def monotonic(l: list):
    if len(l) <= 1:
        return True
    increasing = decreasing = True
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            decreasing = False
        elif l[i] < l[i-1]:
            increasing = False
        if not increasing and not decreasing:
            return False
    return True
