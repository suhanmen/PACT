python
def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = sorted([l[i] for i in even_indices])
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_values.pop(0))
        else:
            result.append(l[i])
    return result
