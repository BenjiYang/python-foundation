###################################################### 字符串encode/decode ######################################################
import chardet
str = "中文"
print("Before encoded string: %s" % str)

strEncoded = str.encode("utf8")
print("After encoded string: %s" % strEncoded)

strDecoded = strEncoded.decode("utf8")
print("After decoded string: %s" % strDecoded)


# 乱码下不知道何种encode时，可以使用工具来解码，如使用库“chardet”
stringUnknown = b'Montr\xe9al'
chardetStr = chardet.detect(stringUnknown)
chardetDecodedStr = chardet.decode(stringUnknown)
print(chardetStr)
print(chardetDecodedStr)
###################################################### 字符串encode/decode ######################################################
