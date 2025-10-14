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
    if len(text) < 2:
        return text
    else:
        result = text.replace(" ", "_")
        consecutive_spaces = False
        for i in range(len(result)-1):
            if result[i] == result[i+1] == "_":
                if consecutive_spaces == False:
                    result = result[:i+1] + "-" + result[i+2:]
                    consecutive_spaces = True
                else:
                    result = result[:i] + "-" + result[i+2:]
            else:
                consecutive_spaces = False
        if result[0] == " ":
            result = "_" + result[1:]
        return result
