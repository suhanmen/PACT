def Strongest_Extension(class_name, extensions):
    strengths = {}
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strengths[extension] = CAP - SM
    strongest = max(strengths, key=strengths.get)
    return f"{class_name}.{strongest}"
