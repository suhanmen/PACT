def Strongest_Extension(class_name, extensions):
    strongest_ext = None
    strongest_ext_strength = float('-inf')
    for ext in extensions:
        cap_count = sum(1 for c in ext if c.isupper())
        sm_count = sum(1 for c in ext if c.islower())
        strength = cap_count - sm_count
        if strength > strongest_ext_strength:
            strongest_ext = ext
            strongest_ext_strength = strength
    return f"{class_name}.{strongest_ext}"
