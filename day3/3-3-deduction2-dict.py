# 字典推导式，给数组key，专成字典并赋值
print({k: "空" for k in ['name', 'age']})


# k,v 通过zip()函数包装，后推导转成字典
k1 = ['name', 'age']
v1 = ['Tom', 10]
print({k: v for k, v in zip(k1, v1)})


# 26个大写字母和序号的字典 1:“A” 2:"B"
letter_dict = {k: chr(64+k) for k in range(1, 27)}
print(letter_dict)

# 26个大写字母和序号的字典 “A”:1 "B":2
letter_dict2 = {chr(64+v): v for v in range(1, 27)}
print(letter_dict2)

# 对换K，V位置
exchangeKV_dict = {'A': 1, 'B': 2, 'C': 3}
print({v: k for k, v in exchangeKV_dict.items()})
