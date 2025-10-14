def Strongest_Extension(class_name, extensions):
    strengths = {}
    for ext in extensions:
        CAP = sum(1 for c in ext if c.isupper())
        SM = sum(1 for c in ext if c.islower())
        strengths[ext] = CAP - SM
    strongest = min(strengths, key=strengths.get)
    result = class_name + '.' + strongest
    return result
