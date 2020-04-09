import hashlib
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()



print(md5("/Users/leolee/photo/photo/20200409/DAL_0001.JPG"))
print(md5("/Users/leolee/photo/DAL_0001.JPG"))
