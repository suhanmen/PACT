def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    strongest_strength = None
    for extension in extensions:
        CAP = 0
        SM = 0
        for letter in extension:
            if letter.isupper():
                CAP += 1
            if letter.islower():
                SM += 1
        strength = CAP - SM
        if strongest_extension is None or strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    return f"{class_name}.{strongest_extension}"
