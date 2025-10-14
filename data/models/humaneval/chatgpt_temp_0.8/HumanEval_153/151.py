def Strongest_Extension(class_name, extensions):
    strongest_extension = extensions[0]
    for extension in extensions:
        cap_count = sum(1 for ch in extension if ch.isupper())
        sm_count = sum(1 for ch in extension if ch.islower())
        strength = cap_count - sm_count
        strongest_cap_count = sum(1 for ch in strongest_extension if ch.isupper())
        strongest_sm_count = sum(1 for ch in strongest_extension if ch.islower())
        strongest_strength = strongest_cap_count - strongest_sm_count
        if strength > strongest_strength or (strength == strongest_strength and extensions.index(extension) < extensions.index(strongest_extension)):
            strongest_extension = extension
    return class_name + '.' + strongest_extension
