def sort_even(l: list):
    even = sorted([x for x in l[::2]])
    return [even.pop(0) if i % 2 == 0 else l[i] for i in range(len(l))]
