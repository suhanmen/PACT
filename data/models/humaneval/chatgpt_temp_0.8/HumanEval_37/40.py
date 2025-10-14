def sort_even(l: list):
    even = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    result = [l[i] if i % 2 != 0 else even.pop(0) for i in range(len(l))]
    return result
