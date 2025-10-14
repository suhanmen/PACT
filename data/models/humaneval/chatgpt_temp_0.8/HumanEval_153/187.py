def Strongest_Extension(class_name, extensions):
    strongest_extension = extensions[0]
    strongest_strength = calculate_strength(strongest_extension)
    for extension in extensions[1:]:
        strength = calculate_strength(extension)
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    return class_name + '.' + strongest_extension
