def Strongest_Extension(class_name, extensions):
    def strength(extension):
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        return CAP - SM

    strongest = max(extensions, key=lambda e: (strength(e), extensions.index(e)))
    return f"{class_name}.{strongest}"
