def Strongest_Extension(class_name, extensions):
    # Initialize variables to hold the strongest extension and its strength
    strongest_ext = ""
    strongest_ext_strength = float("-inf")
    
    # Iterate through the extensions
    for ext in extensions:
        # Calculate the strength of the extension
        cap_count = sum(1 for char in ext if char.isupper())
        sm_count = sum(1 for char in ext if char.islower())
        strength = cap_count - sm_count
        
        # Update the strongest extension if this one is stronger
        if strength > strongest_ext_strength:
            strongest_ext = ext
            strongest_ext_strength = strength
    
    # Return the class name concatenated with the strongest extension
    return f"{class_name}.{strongest_ext}"
