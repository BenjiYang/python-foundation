import os

# print(os.path.isfile(os.getcwd()))
# print('获取当前路径 - \n %s' % os.getcwd())
# print('获取上一层目录下的绝对路径 - \n %s' % os.path.abspath('../'))
# print('获取路径下所有文件和文件夹 - \n %s' % os.listdir())

# os.path.split()
# os.path.join()
# os.path.dirname()
# os.path.basename()


def get_all_file(path):
    for i in os.listdir(path):
        if os.path.isfile(i):
            print(i)
        elif os.path.isdir(i):
            get_all_file(path + "/" + i)


get_all_file(
    "/Users/WenjieYang/Workspace/VisualStidioCodeProject/pythonTraining/day3")
