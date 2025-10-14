python
def Strongest_Extension(class_name, extensions):
    strengths = {}
    for extension in extensions:
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        strengths[extension] = cap_count - sm_count
        
    strongest = max(strengths, key=strengths.get)
    return f"{class_name}.{strongest}"
