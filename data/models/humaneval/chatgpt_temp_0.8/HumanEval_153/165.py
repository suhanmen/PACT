def Strongest_Extension(class_name, extensions):
    strengths = []
    for ext in extensions:
        CAP = sum(map(str.isupper, ext))
        SM = sum(map(str.islower, ext))
        strength = CAP - SM
        strengths.append((strength, ext))
    strongest = max(strengths)
    strongest_ext = strongest[1]
    return class_name + '.' + strongest_ext
