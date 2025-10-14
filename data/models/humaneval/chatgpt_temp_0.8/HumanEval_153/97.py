def Strongest_Extension(class_name, extensions):
    strengths = []
    for ext in extensions:
        CAP = sum(1 for c in ext if c.isupper())
        SM = sum(1 for c in ext if c.islower())
        strength = CAP - SM
        strengths.append(strength)
    max_strength = max(strengths)
    strongest_ext = extensions[strengths.index(max_strength)]
    return f"{class_name}.{strongest_ext}"
