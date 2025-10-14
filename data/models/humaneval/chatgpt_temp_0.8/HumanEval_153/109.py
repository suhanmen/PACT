def Strongest_Extension(class_name, extensions):
    strongest_extension = ""
    strongest_extension_strength = float('-inf')
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        if strength > strongest_extension_strength:
            strongest_extension_strength = strength
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"
