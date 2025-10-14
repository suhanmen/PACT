def Strongest_Extension(class_name, extensions):
    strongest = None
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        if strongest is None or strength > strongest[0]:
            strongest = (strength, extension)
    return f"{class_name}.{strongest[1]}"
