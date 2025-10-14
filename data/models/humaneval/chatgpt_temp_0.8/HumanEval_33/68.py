def sort_third(l: list):
    multiples_of_three = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    return [multiples_of_three.pop(0) if i % 3 == 0 else l[i] for i in range(len(l))]
