def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf') # initialize max_strength to negative infinity
    strongest_extension = None
    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return class_name + '.' + strongest_extension
