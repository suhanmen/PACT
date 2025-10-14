def Strongest_Extension(class_name, extensions):
    strengths = []
    for ext in extensions:
        CAP = len([char for char in ext if char.isupper()])
        SM = len([char for char in ext if char.islower()])
        strength = CAP - SM
        strengths.append(strength)
    max_strength = max(strengths)
    max_index = strengths.index(max_strength)
    strongest_ext = extensions[max_index]
    return class_name + "." + strongest_ext
