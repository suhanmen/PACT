# CANNOT PARSE CODE SNIPPET
def sort_even(l: list) -> list:
    even_nums = sorted([n for i, n in enumerate(l) if i % 2 == 0])
    result = [n if i % 2 != 0 else even_nums[i // 2] for i, n in enumerate(l)]
    return result
