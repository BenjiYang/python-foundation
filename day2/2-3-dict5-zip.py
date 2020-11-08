
###################################################### zip 分解list，再转成dict ######################################################
# zip - 方法快速封装key list 和 vaue list，然后可强制转换成dictionary
keyList = ["name", "age", "city"]
valueList = ["Tom", 25, "guangzhou"]
zip_obj = zip(keyList, valueList)
print(dict(zip_obj))
###################################################### zip 分解list，再转成dict ######################################################
