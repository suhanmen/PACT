def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    longest_str = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest_str):
            longest_str = string
    return longest_str
