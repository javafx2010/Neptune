from crypto.Hash import SHA256


class classif:

    def action(self, file):
        hash_md5 = SHA256.new()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()
