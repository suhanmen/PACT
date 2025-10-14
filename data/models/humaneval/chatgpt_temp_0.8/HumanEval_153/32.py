def Strongest_Extension(class_name, extensions):
    strengths = [(extension, sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())) for extension in extensions]
    strongest = max(strengths, key=lambda x: x[1])
    strongest_extensions = [extension for extension in strengths if extension[1] == strongest[1]]
    return f"{class_name}.{strongest_extensions[0][0]}"
