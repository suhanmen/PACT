def Strongest_Extension(class_name, extensions):
    strongest_ext = ''
    strength = float('-inf')
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        ext_strength = cap - sm
        if ext_strength > strength:
            strength = ext_strength
            strongest_ext = ext
    return f"{class_name}.{strongest_ext}"
