from django.shortcuts import render
from django.http import HttpResponse
from contact.models import Contact

# Create your views here.


# 导入HttpResponse, 定义视图函数


def index(request):
    return HttpResponse("Hello Django!!")


# 定义新的视图函数，用于返回HTML页面信息
def home(request):
    return render(request, "magicpage.html")


# 定义方法获取数据库数据
def get_all_contact(request):
    contact_lists = Contact.objects.all().values()
    print(contact_lists)
    import json
    data = json.dumps(list(contact_lists))
    return HttpResponse(data, content_type="application/json")


# 定义html包含data渲染的视图方法 - mock
def html_mock_data(request):
    # 1）简单点，data自定义一个 people_list
    people_list = [{"name": "Tony", "age": 40}, {"name": "Jenny", "age": 50}]

    # 1）重新声明用key去读取这个list
    mycontext = {"people_list": people_list}

    # render第三个参数context里传入数据的context给模版“htmldata.html"文件里
    return render(request, "htmldata.html", context=mycontext)


# 定义html包含data渲染的视图方法 - db
def html_db_data(request):
    # 2）从数据库来的数据
    contact_list = Contact.objects.all()
    dbcontext = {"contact_list": contact_list}

    # render第三个参数context里传入数据的context给模版“htmldata.html"文件里
    return render(request, "htmldata2.html", context=dbcontext)


# 定义页面跳转详情页，接收多个参数request, id
def detail(request, id):
    contact = Contact.objects.get(id=id)
    convert2Dict = {"contact": contact}
    return render(request, "detail.html", context=convert2Dict)


def register(request):
    return render(request, "register.html")


def save_data(request):
    from contact.tools import gen_password
    # 获取前端表单数据
    username = request.POST.get("username")
    phone_num = request.POST.get("phone_num")
    password = request.POST.get("password")
    password = gen_password(password)
    print(username, phone_num, password)

    Contact.objects.create(
        name=username, phone_num=phone_num, password=password)
    return HttpResponse("数据保存成功！")
