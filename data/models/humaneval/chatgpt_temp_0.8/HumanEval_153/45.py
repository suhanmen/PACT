def Strongest_Extension(class_name, extensions):
    strengths = {}
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        if strength not in strengths:
            strengths[strength] = extension
    max_strength = max(strengths.keys())
    return class_name + '.' + strengths[max_strength]
