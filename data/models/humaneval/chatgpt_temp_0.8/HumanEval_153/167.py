def Strongest_Extension(class_name, extensions):
    strongest_ext = ''
    max_strength = float('-inf')
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            strongest_ext = ext
    return f"{class_name}.{strongest_ext}"
