def Strongest_Extension(class_name, extensions):
    strongest_ext = None
    max_strength = float('-inf')
    for ext in extensions:
        CAP = sum(1 for c in ext if c.isupper())
        SM = sum(1 for c in ext if c.islower())
        strength = CAP - SM
        if strength > max_strength:
            max_strength = strength
            strongest_ext = ext
    return f"{class_name}.{strongest_ext}"
