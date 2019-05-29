import os
import uuid

from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from mangerapp.models import TBook


def index(request):
    return render(request,'index.html')
def add(request):
    return render(request,'main/add.html')
def addlogic(request):#添加书本逻辑，接收表单中的值
    productname=request.POST.get("productname")#商品名称
    author=request.POST.get("author")#作者
    press=request.POST.get("press")#出版社
    publication_time=request.POST.get("publication_time")#出版时间
    market_price=request.POST.get("market_price")#原价/市场价
    dangdang_price=request.POST.get("dangdang_price")#当当价
    pics=request.FILES.get("book_price")#书籍图片
    if productname and author and press and publication_time and market_price and dangdang_price: #判断值是否为空
        ext=os.path.splitext(pics.name)[1]#切割出文件的后缀名
        pics.name=str(uuid.uuid4())+ext #随机生成文件名并拼接上切割出来的原文件的后缀名
        #向数据库的book表插入数据
        insert=TBook.objects.create(book_name=productname,anthor=author,book_publish=press,pushish_time=publication_time,market_price=market_price,dangdang_price=dangdang_price,pics=pics)
        #如果插入成功
        if insert:
            #返回提示信息
            return HttpResponse("提交成功")
        return HttpResponse("提交失败")
    return HttpResponse("不能为空")
def dzlist(request):
    return render(request,'main/dzlist.html')
def list(request):
    select=TBook.objects.all()
    return render(request,'main/list.html',{"select":select})
def splb(request):
    return render(request,'main/splb.html')
def test(request):
    return render(request,'main/test.html')
def zjsp(request):
    return render(request,'main/zjsp.html')
def zjzlb(request):
    return render(request,'main/zjzlb.html')