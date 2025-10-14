def Strongest_Extension(class_name, extensions):
    strengths = {}
    for ext in extensions:
        CAP = sum(1 for c in ext if c.isupper())
        SM = sum(1 for c in ext if c.islower())
        strength = CAP - SM
        strengths[ext] = strength
    strongest_ext = max(strengths, key=strengths.get)
    return f"{class_name}.{strongest_ext}"
