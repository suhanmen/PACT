def Strongest_Extension(class_name, extensions):
    strongest_name = ""
    strongest_strength = float("-inf")
    for extension in extensions:
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        strength = cap_count - sm_count
        if strength > strongest_strength:
            strongest_name = extension
            strongest_strength = strength
    return f"{class_name}.{strongest_name}"
