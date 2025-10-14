def Strongest_Extension(class_name, extensions):
    strengths = {}
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        strengths[extension] = strength
    sorted_strengths = sorted(strengths.items(), key=lambda x: (x[1], extensions.index(x[0])))
    strongest_extension = sorted_strengths[-1][0]
    return f"{class_name}.{strongest_extension}"
