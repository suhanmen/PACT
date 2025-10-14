def Strongest_Extension(class_name, extensions):
    strongest = None
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if strongest is None or strength > strongest[1] or (strength == strongest[1] and extensions.index(ext) < extensions.index(strongest[0])):
            strongest = (ext, strength)
    return f"{class_name}.{strongest[0]}"
