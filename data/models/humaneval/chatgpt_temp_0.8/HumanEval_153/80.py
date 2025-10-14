def Strongest_Extension(class_name, extensions):
    strongest_ext = None
    strongest_strength = float('-inf')
    for ext in extensions:
        CAP = sum(1 for c in ext if c.isupper())
        SM = sum(1 for c in ext if c.islower())
        strength = CAP - SM
        if strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = strength
    return class_name + '.' + strongest_ext
