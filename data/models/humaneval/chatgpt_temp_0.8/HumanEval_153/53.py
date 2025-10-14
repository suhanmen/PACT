def Strongest_Extension(class_name, extensions):
    strongest = None
    for extension in extensions:
        cap = sum(1 for letter in extension if letter.isupper())
        sm = sum(1 for letter in extension if letter.islower())
        strength = cap - sm
        if strongest is None or strength > strongest[0]:
            strongest = (strength, extension)
    return class_name + '.' + strongest[1]
