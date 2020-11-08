
1.1新建项目
> django-admin startproject hello_django

1.2启动django项目
> python3 manage.py runserver

1.3访问启动地址, 浏览器打开地址
> http://127.0.0.1:8000/



2 - 和普通文本交互
2.1 基于现有的脚手架，创建自己的app，如contact
> python3 manage.py startapp contact
运行完上条命令后，将会生成一个‘contact’的文件夹，里面包含‘migrations’文件夹和其他相关的.py文件

2.2 修改settings.py，添加注册自己的app名字，如contact
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册自己的app
    'contact',
]
```

2.3 修改 contact - views.py，创建视图函数
```python
# 导入HttpResponse, 定义视图函数
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Django!!")
```

2.4 绑定路由 - 修改url.py，设置url地址映射
```python
from contact.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 添加地址映射规则，没有uri情况下，视图操作调用index方法
    url(r'^$', index),
]
```

2.5 再次访问启动地址, 浏览器打开地址，默认返回"Hello Django!!"
> http://127.0.0.1:8000/



3 - 和HTML交互
3.1 为了能返回HTML页面，在项目根目录下创建‘templates’文件夹

3.2 修改settings.py, DIRS里添加刚刚创建的‘templates’文件夹路径
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS里添加templates的路径
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

3.3 在‘templates’文件夹下加入任意含内容的HTML文件，如'magicpage.html'

3.4 修改 contact - views.py，创建新的视图函数
```python
# 定义新的视图函数，用于返回HTML页面信息
def home(request):
    return render(request, "magicpage.html")
```

3.5 绑定路由 - 修改url.py，设置url地址映射
```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 添加地址映射规则
    url(r'^$', index),
    # 添加地址映射规则 - 返回html文件
    url(r'^home/$', home),
]
```

3.6 再次访问启动地址, 浏览器打开如下地址，返回html文件
> http://127.0.0.1:8000/home/



4 - 为了能和数据库交互，定义数据库表模型，生成数据库表
4.1 创建表模型，修改contact - models.py文件
```python
class Contact(models.Model):
    # 定模型含有属性，及相应属性值长度
    name = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=11)
    password = models.CharField(max_length=400)
```

4.2 makemigrations - 执行命令，使用python大管家“manage.py”来操作(makemigrations)，声明模型信息，用于与数据库交互
```shell
$ python3 manage.py makemigrations
Migrations for 'contact':
  contact/migrations/0001_initial.py
    - Create model Contact
```

4.3 migrate - 执行命令，使用python大管家“manage.py”来操作(migrate)，声明模型信息，用于与数据库交互
```shell
$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contact, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying contact.0001_initial... OK
  Applying sessions.0001_initial... OK
```

4.4 命令行查看数据库信息，输入“sqlite3”
```shell
Benji:hello_django WenjieYang$ sqlite3 db.sqlite3
SQLite version 3.28.0 2019-04-15 14:49:49
Enter ".help" for usage hints.
sqlite> .tables
auth_group                  contact_contact           
auth_group_permissions      django_admin_log          
auth_permission             django_content_type       
auth_user                   django_migrations         
auth_user_groups            django_session            
auth_user_user_permissions
sqlite> select * from contact_contact;
1|Alex|15912341234|1234
2|Ben|15823452345|2345
3|Christy|15734563456|3456
4|David|13645674567|ChangedPwd
6|test1|12345678901|ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413
sqlite> 
```


5 - 使用Django后台查看创建完的表
5.1 createsuperuser - manage.py 创建Django后台账号
```shell
$ python3 manage.py createsuperuser
Username (leave blank to use 'wenjieyang'): admin
Email address: 
Password: 
Password (again): 
Superuser created successfully.
```

5.2 settings自定义后台语言和时区，
```python
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
```

5.3 使用刚刚创建的后台账户密码访问
> http://127.0.0.1:8000/admin/

5.4 将注册app的模型导入到admin后台，才能看到信息，修改contact - admin.py
```python
from contact.models import Contact
# 导入模块Contact，并注册上
admin.site.register(Contact)
```

5.5 使用刚刚创建的后台账户密码访问，刷新后可以看到‘Contact’表
> http://127.0.0.1:8000/admin/

5.6 在admin 后台UI中，对表Contact插入几条数据


6 通过模型做增删改查
6.1 执行如下命令进入shell
> python3 manage.py shell

6.2 运行相关命令做增删改查
```python
from contact.models import Contact

# 新增数据（新增后UI中可查看）
Contact.objects.create(name="David", phone_num="13645674567", password="4567")

# 查找某个数据
contact_search = Contact.objects.get(name="Alex")

# 查找所有数据
contact_list = Contact.objects.all()

# 删除数据
Contact.objects.create(name="Zed", phone_num="13699998888", password="9988")

c1 = Contact.objects.get(name="Zed")
c1.delete()

# 修改数据
c2 = Contact.objects.get(name="David")
c2.password = "ChangedPwd"
c2.save()
```



7 - 后台查找的数据以接口的形式返回
7.1 在contact - views.py写一个接口
```python
from contact.models import Contact

# 定义方法获取数据库数据
def get_all_contact(request):
    contact_lists = Contact.objects.all().values()
    print(contact_lists)
    import json
    data = json.dumps(contact_lists)
    return HttpResponse(data, content_type="application/json")
```

7.2 增加绑定路由，在urls.py，然后访问页面查看改动
```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 添加地址映射规则
    url(r'^$', index),
    # 添加地址映射规则 - 返回html文件
    url(r'^home/$', home),
    # 添加地址映射规则 - 返回数据库表信息
    url(r'^contacts/$', get_all_contact)
]
```

7.3 访问页面看效果
> http://127.0.0.1:8000/contacts/


8 利用模版方法，返回带有数据的HTML页面
8.1 urls.py 绑定路由规则
```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 添加地址映射规则
    url(r'^$', index),
    # 添加地址映射规则 - 返回html文件
    url(r'^home/$', home),
    # 添加地址映射规则 - 返回数据库表信息
    url(r'^contacts/$', get_all_contact),
    # 添加地址印社规则 - 返回html含数据库数据
    url(r'^htmldata/$', html_db_data),
]
```

8.2 contact - views.py 视图方法定义
```python
# 定义html包含data渲染的视图方法
def html_db_data(request):
    # 简单点，data自定义一个 people_list
    people_list = [{"name": "Tony", "age": 40}, {"name": "Jenny", "age": 50}]

    # 重新声明用key去读取这个list
    mycontext = {"people_list": people_list}

    # render第三个参数context里传入数据的context给模版“htmldata.html"文件里
    return render(request, "htmldata.html", context=mycontext)
```

8.3 模版文件中的"htmldata.html"，引用传入的context数据
```html
...
<body>
    {{people_list}}
</body>
```

8.4 访问页面看效果
> http://127.0.0.1:8000/htmldata/


9 开发列表详情页

10 练习作业：开发一个注册系统，注册表单数据包括：姓名，电话号码，密码，将注册的用户信息保存到数据库中



```python
```
```python
```
```python
```