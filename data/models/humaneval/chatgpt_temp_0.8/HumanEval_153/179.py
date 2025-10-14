def Strongest_Extension(class_name, extensions):
    def strength(extension):
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        return CAP - SM
    
    strongest = extensions[0]
    for ext in extensions[1:]:
        if strength(ext) > strength(strongest):
            strongest = ext
            
    return class_name + '.' + strongest
