# CANNOT PARSE CODE SNIPPET
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i != 0:
            result.append(delimiter)
        result.append(num)
    return result
