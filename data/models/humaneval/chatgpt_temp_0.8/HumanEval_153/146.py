def Strongest_Extension(class_name, extensions):
    def strength(extension):
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        return cap_count - sm_count

    strongest_extension = None
    for extension in extensions:
        if strongest_extension is None or strength(extension) > strength(strongest_extension):
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"
