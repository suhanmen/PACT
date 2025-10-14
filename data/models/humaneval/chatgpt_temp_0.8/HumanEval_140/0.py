def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    result_str = ""
    prev_char = ""
    count_spaces = 0
    for char in text:
        if char == " ":
            count_spaces += 1
            if count_spaces == 3:
                result_str += "-"
                count_spaces = 0
        else:
            if count_spaces > 0:
                if prev_char != " ":
                    result_str += "_"
                else:
                    result_str += "-"
            count_spaces = 0
            result_str += char
        prev_char = char
    if count_spaces > 0:
        if prev_char != " ":
            result_str += "_"
        else:
            result_str += "-"
    return result_str
