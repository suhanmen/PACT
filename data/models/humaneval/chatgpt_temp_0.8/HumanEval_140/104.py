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
    if len(text) < 3:
        return text.replace(" ", "_")
    else:
        new_text = ""
        spaces_count = 0
        for i in range(len(text)):
            if text[i] == " ":
                spaces_count += 1
                if spaces_count == 3:
                    new_text += "-"
                    spaces_count = 0
            else:
                if spaces_count > 0:
                    new_text += "_"
                    spaces_count = 0
                new_text += text[i]
        if spaces_count > 0:
            new_text += "_" * spaces_count
        return new_text
