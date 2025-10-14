def Strongest_Extension(class_name, extensions):
    strongest_ext = None
    strongest_strength = None
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if strongest_ext is None or strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = strength
    return f"{class_name}.{strongest_ext}"
