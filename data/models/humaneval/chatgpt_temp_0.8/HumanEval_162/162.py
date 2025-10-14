import hashlib

def string_to_md5(text):
    if not text:
        return None
    else:
        md5 = hashlib.md5()
        md5.update(text.encode('utf-8'))
        return md5.hexdigest()
