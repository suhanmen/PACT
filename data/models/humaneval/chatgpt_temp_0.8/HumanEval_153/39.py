def Strongest_Extension(class_name, extensions):
    strongest_ext = ''
    strongest_strength = float('-inf')
    for ext in extensions:
        CAP = sum(1 for c in ext if c.isupper())
        SM = sum(1 for c in ext if c.islower())
        strength = CAP - SM
        if strength > strongest_strength:
            strongest_strength = strength
            strongest_ext = ext
    return f"{class_name}.{strongest_ext}"
