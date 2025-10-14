import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # Create an MD5 hash object
    md5 = hashlib.md5()

    # Update the hash object with the text
    md5.update(text.encode())

    # Return the hexadecimal representation of the hash
    return md5.hexdigest()
