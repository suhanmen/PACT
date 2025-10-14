def Strongest_Extension(class_name, extensions):
    strengths = []
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        strengths.append(strength)
    max_strength = max(strengths)
    max_strength_indices = [i for i, strength in enumerate(strengths) if strength == max_strength]
    strongest_extension = extensions[max_strength_indices[0]]
    return class_name + '.' + strongest_extension
