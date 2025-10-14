def Strongest_Extension(class_name, extensions):
    strongest = extensions[0]
    for ext in extensions:
        CAP = sum(1 for c in ext if c.isupper())
        SM = sum(1 for c in ext if c.islower())
        strength = CAP - SM
        if strength > (sum(1 for c in strongest if c.isupper()) - sum(1 for c in strongest if c.islower())):
            strongest = ext
    return class_name + '.' + strongest
