def Strongest_Extension(class_name, extensions):
    strongest_extension = ""
    strongest_strength = float('-inf')
    for extension in extensions:
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        strength = cap_count - sm_count
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    return class_name + "." + strongest_extension
