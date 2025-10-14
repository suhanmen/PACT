def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers """
    return [value for value in values if type(value) == int]
