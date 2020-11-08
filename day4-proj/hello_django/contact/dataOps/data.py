from contact.models import Contact

# 查找某个数据
contact_search = Contact.objects.get(name="Alex")
print("查找某个数据 - %s" % contact_search)
# 查找所有数据
contact_list = Contact.objects.all()
print("查找所有数据 - %s" % contact_list)

# 新增数据
Contact.objects.create(name="David", phone_num="13645674567", password="4567")
print("新增后的数据 - %s" % Contact.objects.get(name="David"))


# 删除数据
Contact.objects.create(name="Zed", phone_num="13699998888", password="9988")
print("数据创造用于删除 - %s" % Contact.objects.get(name="Zed"))
c1 = Contact.objecst.get(name="Zed")
c1.delete()
print("数据删除后再次搜索 - %s" % Contact.objects.get(name="Zed"))

# 修改数据
c2 = Contact.objects.get(name="David")
print('修改前数据 - %s' % c2)
c2.password = "ChangedPwd"
c2.save()
print('修改后数据 - %s' % c2)
