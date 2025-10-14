def Strongest_Extension(class_name, extensions):
    strengths = {}
    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        if strength not in strengths:
            strengths[strength] = []
        strengths[strength].append(extension)
    max_strength = max(strengths.keys())
    return class_name + '.' + strengths[max_strength][0]
