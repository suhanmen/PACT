def Strongest_Extension(class_name, extensions):
    strongest = None
    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        if strongest is None or strength > strongest[1] or (strength == strongest[1] and extensions.index(extension) < extensions.index(strongest[0])):
            strongest = (extension, strength)
    return class_name + '.' + strongest[0]
