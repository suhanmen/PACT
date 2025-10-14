def Strongest_Extension(class_name, extensions):
    strengths = []
    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        strengths.append(strength)
    max_strength = max(strengths)
    index_of_max_strength = strengths.index(max_strength)
    strongest_extension_name = extensions[index_of_max_strength]
    return class_name + '.' + strongest_extension_name
