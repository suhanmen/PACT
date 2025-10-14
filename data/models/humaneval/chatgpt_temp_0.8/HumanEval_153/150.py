def Strongest_Extension(class_name, extensions):
    strongest = None
    for extension in extensions:
        strength = extension.count('A-Z') - extension.count('a-z')
        if strongest is None or strength > strongest[0]:
            strongest = (strength, extension)
    return f"{class_name}.{strongest[1]}"
