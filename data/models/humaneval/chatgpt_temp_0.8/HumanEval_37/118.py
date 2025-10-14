def sort_even(l: list):
    # Extract the even-indexed elements from the input list
    even_indices = range(0, len(l), 2)
    even_elements = [l[i] for i in even_indices]

    # Sort the even elements
    sorted_even = sorted(even_elements)

    # Create a new list with the same odd-indexed elements as the input list
    # and the sorted even-indexed elements
    result = [None] * len(l)
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = sorted_even[i // 2]
        else:
            result[i] = l[i]

    return result
