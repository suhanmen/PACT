def odd_count(lst):
    result = []
    for s in lst:
        count = sum(1 for c in s if int(c) % 2 != 0)
        result.append(f"the number of odd elements {count}n the str{lst.index(s)}ng {s} of the {lst.index(s)}nput.")
    return result
