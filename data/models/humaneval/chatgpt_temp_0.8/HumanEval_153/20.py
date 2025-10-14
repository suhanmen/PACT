def Strongest_Extension(class_name, extensions):
    strengths = {}
    for extension in extensions:
        CAP = len([char for char in extension if char.isupper()])
        SM = len([char for char in extension if char.islower()])
        strength = CAP - SM
        strengths[extension] = strength
    strongest = max(strengths, key=strengths.get)
    return f"{class_name}.{strongest}"
