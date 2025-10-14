def Strongest_Extension(class_name, extensions):
    strongest = None
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        strength = cap - sm
        if strongest is None or strength > strongest[1]:
            strongest = (e, strength)
    return f"{class_name}.{strongest[0]}"
