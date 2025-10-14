def odd_count(lst):
    result = []
    for s in lst:
        odd_count = len([c for c in s if int(c) % 2 == 1])
        result.append(f"the number of odd elements {odd_count}n the str{lst.index(s)}ng {s} of the {lst.index(s)}nput.")
    return result
