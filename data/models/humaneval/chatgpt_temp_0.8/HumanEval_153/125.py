def Strongest_Extension(class_name, extensions):
    strengths = []
    for extension in extensions:
        cap = sum(1 for letter in extension if letter.isupper())
        sm = sum(1 for letter in extension if letter.islower())
        strength = cap - sm
        strengths.append((strength, extension))
    strengths.sort(reverse=True)
    strongest = strengths[0][1]
    for strength, extension in strengths[1:]:
        if strength != strengths[0][0]:
            break
        if extensions.index(extension) < extensions.index(strongest):
            strongest = extension
    return f"{class_name}.{strongest}"
