def sort_even(l: list):
    even = sorted([l[i] for i in range(len(l)) if i%2 == 0])
    return [even[i//2] if i%2 == 0 else l[i] for i in range(len(l))]
