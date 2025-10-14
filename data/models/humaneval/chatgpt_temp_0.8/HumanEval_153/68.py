def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    strongest_strength = None
    
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        
        if strongest_extension is None or strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    
    return f"{class_name}.{strongest_extension}"
