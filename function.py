import hashlib


class Hash:
    def __init__(self):
        pass

    def md5(self, _txt):
        return hashlib.md5(_txt.encode()).hexdigest()

    def sha1(self, _txt):
        return hashlib.sha1(_txt.encode()).hexdigest()

    def sha256(self, _txt):
        return hashlib.sha256(_txt.encode()).hexdigest()

    def sha512(self, _txt):
        return hashlib.sha512(_txt.encode()).hexdigest()
