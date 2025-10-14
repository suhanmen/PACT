python
def Strongest_Extension(class_name, extensions):
    strongest_extension = extensions[0]
    strongest_strength = len([c for c in strongest_extension if c.isupper()]) - len([c for c in strongest_extension if c.islower()])
    for extension in extensions[1:]:
        strength = len([c for c in extension if c.isupper()]) - len([c for c in extension if c.islower()])
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    return f"{class_name}.{strongest_extension}"
