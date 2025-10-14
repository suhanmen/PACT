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
    underscores = text.replace(" ", "_")  # replace spaces with underscores
    consecutive_spaces = underscores.replace("__", "-")  # replace consecutive underscores with a hyphen
    while "__" in consecutive_spaces:  # repeat until there are no more consecutive underscores
        consecutive_spaces = consecutive_spaces.replace("__", "-")
    if consecutive_spaces.startswith(" "):  # if there is a space at the beginning of the string
        consecutive_spaces = "_" + consecutive_spaces[1:]  # replace it with an underscore
    return consecutive_spaces
