def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    if min_num == max_num:
        return [0.0 for num in numbers]
    return [(num - min_num) / (max_num - min_num) for num in numbers]
