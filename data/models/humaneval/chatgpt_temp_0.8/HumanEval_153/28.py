def Strongest_Extension(class_name, extensions):
    strengths = []
    for ext in extensions:
        CAP = len([c for c in ext if c.isupper()])
        SM = len([c for c in ext if c.islower()])
        strength = CAP - SM
        strengths.append(strength)
    max_strength = max(strengths)
    max_strength_indices = [i for i, s in enumerate(strengths) if s == max_strength]
    strongest_extension_index = min(max_strength_indices)
    strongest_extension = extensions[strongest_extension_index]
    return class_name + '.' + strongest_extension
