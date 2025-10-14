def Strongest_Extension(class_name, extensions):
    strengths = []
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strengths.append((ext, cap - sm))
    strengths.sort(key=lambda x: (-x[1], extensions.index(x[0])))
    return f"{class_name}.{strengths[0][0]}"
