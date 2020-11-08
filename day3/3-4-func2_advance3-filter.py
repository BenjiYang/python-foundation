###################### filter ######################
filter_obj1 = filter(lambda x: x > 2, [1, 2, 4, 5])
print(list(filter_obj1))

filter_obj2 = filter(lambda x: isinstance(x, str), [1, 2, 3, 'A', 'B', 'C'])
print(type(filter_obj2))
print(filter_obj2)
print(list(filter_obj2))
###################### filter ######################
