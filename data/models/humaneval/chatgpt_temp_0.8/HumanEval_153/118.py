def Strongest_Extension(class_name, extensions):
    strengths = []
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        strengths.append((strength, extension))
    strongest = max(strengths, key=lambda x: x[0])[1]
    return f"{class_name}.{strongest}"
