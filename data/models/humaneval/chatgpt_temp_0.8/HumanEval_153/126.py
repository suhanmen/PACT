def Strongest_Extension(class_name, extensions):
    strongest_ext = extensions[0]
    strongest_strength = calculate_strength(strongest_ext)
    
    for ext in extensions:
        strength = calculate_strength(ext)
        if strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = strength
    
    return class_name + '.' + strongest_ext
