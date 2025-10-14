def count_distinct_characters(string: str) -> int:
    distinct_chars = set(string.lower())
    return len(distinct_chars)
