def Strongest_Extension(class_name, extensions):
    strongest = None
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        if strongest is None or strength > strongest[1] or (strength == strongest[1] and extensions.index(extension) < extensions.index(strongest[0])):
            strongest = (extension, strength)
    return class_name + "." + strongest[0]
