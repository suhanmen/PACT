def Strongest_Extension(class_name, extensions):
    strongest_extension = ""
    strength = float('-inf') # initialize strength as negative infinity
    for extension in extensions:
        cap_count = sum(1 for c in extension if c.isupper()) # count uppercase letters
        sm_count = sum(1 for c in extension if c.islower()) # count lowercase letters
        extension_strength = cap_count - sm_count
        if extension_strength > strength:
            strength = extension_strength
            strongest_extension = extension
    return class_name + '.' + strongest_extension
