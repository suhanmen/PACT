# CANNOT PARSE CODE SNIPPET
def sort_even(l: list) -> list:
    even_values = sorted([x for i, x in enumerate(l) if i % 2 == 0])
    result = []
    for i, x in enumerate(l):
        if i % 2 == 0:
            result.append(even_values.pop(0))
        else:
            result.append(x)
    return result
