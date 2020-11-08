# 1
i = 0
while i < 10:
    print(i)
    i += 1

print('\n')

# i=5时跳过
i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
