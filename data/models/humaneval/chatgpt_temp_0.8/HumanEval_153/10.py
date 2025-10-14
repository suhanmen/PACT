def Strongest_Extension(class_name, extensions):
    strongest = None
    for extension in extensions:
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        strength = cap_count - sm_count
        if strongest is None or strength < strongest[0]:
            strongest = (strength, extension)
    return f"{class_name}.{strongest[1]}"
