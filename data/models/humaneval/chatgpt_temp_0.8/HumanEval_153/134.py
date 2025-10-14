def Strongest_Extension(class_name, extensions):
    strongest_ext = ""
    strongest_strength = None
    for ext in extensions:
        cap_letters = sum(1 for c in ext if c.isupper())
        sm_letters = sum(1 for c in ext if c.islower())
        strength = cap_letters - sm_letters
        if strongest_strength is None or strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = strength
    return f"{class_name}.{strongest_ext}"
