def fix_spaces(text):
    result = ""
    spaces_count = 0
    for char in text:
        if char == " ":
            spaces_count += 1
            if spaces_count > 2:
                result += "-"
            else:
                result += "_"
        else:
            spaces_count = 0
            result += char
    return result
