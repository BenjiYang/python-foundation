"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from contact.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 添加地址映射规则
    url(r'^$', index),
    # 添加地址映射规则 - 返回html文件
    url(r'^home/$', home),
    # 添加地址映射规则 - 返回数据库表信息
    url(r'^contacts/$', get_all_contact),
    # 添加地址印社规则 - 返回html含数据库数据
    url(r'^htmldata/$', html_mock_data),
    url(r'^htmldata2/$', html_db_data),
    # URL 传递 id 的数字参数，给视图处理方法detail
    url(r'^detail/(\d+)/$', detail),
    url(r'^register/$', register),
    url(r'^save_data/$', save_data),
]
