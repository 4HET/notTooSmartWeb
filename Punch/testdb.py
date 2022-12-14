from django.http import HttpResponse

from Punch.models import User

def testdb(request):
    test1 = User(username='', password='')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
def insert(request):
    test1 = User(username='', password="")
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

def delete(request):
    # 删除id=1的数据
    test1 = User.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")


# 数据库操作
# 数据库操作
def select(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = User.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = User.objects.filter(id=1)

    # 获取单个对象
    # response3 = User.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # User.objects.order_by('name')[0:2]

    # 数据排序
    # User.objects.order_by("id")

    # 上面的方法可以连锁使用
    # User.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.username + " " + var.password
    response = response1
    return HttpResponse("<p>" + response + "</p>")

