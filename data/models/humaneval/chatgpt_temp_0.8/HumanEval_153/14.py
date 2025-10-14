def Strongest_Extension(class_name, extensions):
    strengths = []
    for ext in extensions:
        CAP = len([c for c in ext if c.isupper()])
        SM = len([c for c in ext if c.islower()])
        strengths.append((ext, CAP - SM))
    strengths.sort(key=lambda x: x[1], reverse=True)
    strongest_ext = strengths[0][0]
    return f"{class_name}.{strongest_ext}"
