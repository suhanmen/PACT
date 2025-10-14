def Strongest_Extension(class_name, extensions):
    strongest = None
    for ext in extensions:
        CAP = sum(1 for c in ext if c.isupper())
        SM = sum(1 for c in ext if c.islower())
        strength = CAP - SM
        if not strongest or strength > strongest[0]:
            strongest = (strength, ext)
    return f"{class_name}.{strongest[1]}"
