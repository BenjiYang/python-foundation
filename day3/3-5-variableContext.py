# 变量的作用域 LCGB -- 本地变量(Local) < enclosing function (C) < Global < Built-in
MY_GLOBAL_VARIABLE = 'global'


def say_hello():
    my_internal_variable = 'internal'
    print(my_internal_variable)

    MY_GLOBAL_VARIABLE = 'GLOBAL'
    print(MY_GLOBAL_VARIABLE)

    MY_GLOBAL_VARIABLE = 'GLOBAL - Re-assign would failed'
    print(MY_GLOBAL_VARIABLE)


say_hello()
