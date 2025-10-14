import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # create md5 hash object
    md5_hash = hashlib.md5()

    # update hash object with text
    md5_hash.update(text.encode('utf-8'))

    # return hexadecimal digest of hash object
    return md5_hash.hexdigest()
