def Strongest_Extension(class_name, extensions):
    strongest_extension = ""
    strongest_strength = float("-inf")
    for extension in extensions:
        # Calculate the strength of the extension
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        
        # Update the strongest extension if this one is stronger
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    
    # Return the strongest extension in the correct format
    return f"{class_name}.{strongest_extension}"
