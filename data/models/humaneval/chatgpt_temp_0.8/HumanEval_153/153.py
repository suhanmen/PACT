def Strongest_Extension(class_name, extensions):
    strongest_name = None
    strongest_strength = float('-inf')
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        if strength > strongest_strength:
            strongest_strength = strength
            strongest_name = extension
    return f"{class_name}.{strongest_name}"
