def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_extension = ''
    for extension in extensions:
        CAP = len([c for c in extension if c.isupper()])
        SM = len([c for c in extension if c.islower()])
        strength = CAP - SM
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"
