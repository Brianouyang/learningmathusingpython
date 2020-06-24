import hashlib
u1=hashlib.md5("hello world!".encode("utf-8")).hexdigest()
u2=hashlib.sha1("hello world!".encode("utf-8")).hexdigest()
print(u1)
print(u2)
