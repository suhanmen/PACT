def Strongest_Extension(class_name, extensions):
    strongest_ext = ""
    strongest_strength = float('-inf')
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = strength
    return class_name + "." + strongest_ext
