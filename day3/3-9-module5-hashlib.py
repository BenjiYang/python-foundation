import hashlib


str1 = "Tom"

md5_encrpyt = hashlib.md5()
md5_encrpyt.update(str1.encode("utf-8"))
print(str1)
print(md5_encrpyt.hexdigest)

sha512_encrpt = hashlib.sha512()
sha512_encrpt.update(str1.encode("utf-8"))
print(str1)
print(sha512_encrpt.hexdigest)


# 总结  hash后不可逆，但hash后是唯一的值，后续加密后再对比是否一致，如hash pwd
