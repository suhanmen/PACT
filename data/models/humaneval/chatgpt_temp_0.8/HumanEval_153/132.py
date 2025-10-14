def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    max_extension = ""
    for extension in extensions:
        strength = sum(1 if c.isupper() else -1 if c.islower() else 0 for c in extension)
        if strength > max_strength:
            max_strength = strength
            max_extension = extension
    return class_name + "." + max_extension
