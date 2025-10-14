def Strongest_Extension(class_name, extensions):
    strengths = []
    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        strengths.append((strength, extension))
    strengths.sort(reverse=True)
    strongest_extension = strengths[0][1] if strengths else ""
    return f"{class_name}.{strongest_extension}"
