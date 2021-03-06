import hashlib


class classif:

    def action(self, file):
        hash_md5 = hashlib.md5()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(1024*80), b""):
                hash_md5.update(chunk)
            f.close()

        return hash_md5.hexdigest()
