import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # Create an md5 hash object
    md5_hash = hashlib.md5()

    # Encode the string into bytes and update the hash object
    md5_hash.update(text.encode())

    # Get the hexadecimal equivalent of the hash
    return md5_hash.hexdigest()
