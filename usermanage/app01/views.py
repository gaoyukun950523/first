from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from django import views
from django.utils.decorators import method_decorator
from django.conf.urls.static import static
from django.conf import settings
import json
import os
# Create your views here.

# def outer(some_fun):
#     def inner(request,*args,**kwargs):
#         print(request.method)
#         return some_fun(request,*args,**kwargs)
#     return inner
class Login(views.View):
    def dispatch(self, request, *args, **kwargs):
        ret=super(Login,self).dispatch(request,*args,**kwargs)
        return ret
    def get(self,request,*args,**kwargs):
        print("gettttttttt")
        return render(request,"login.html")
    def post(self,req,*args,**kwargs):
        user=req.POST.get("username")
        pwd=req.POST.get("password")
        rep=redirect("/index")
        rep.set_cookie("username",user)
        rep.set_cookie("password",pwd)
        return rep

def login(req):
    if req.method=="POST":
        user=req.POST.get("username")
        pwd=req.POST.get("password")
        rep=redirect("/index")
        rep.set_cookie("username",user)
        rep.set_cookie("password",pwd)
        return rep
    return render(req,"login.html")
def index(req):
    user=req.COOKIES.get("username")
    password=req.COOKIES.get("password")
    if user and password:
        return render(req,"index.html")
    else:
        return redirect("/login")


def classes(req):  #此处采用切片方式进行分页
    if req.method=="GET":
        p=req.GET.get("p",1)
        p=int(p)
        start=(p-1)*5
        end=p*5
        clases=models.Classes.objects.all()[start:end]
        count=models.Classes.objects.all().count()
        a,v=divmod(count,5)  #得到余数
        href_list=[]
        for i in range(a+1):
            ahref="<a href='/classes?p=%s'>%s</a>"%(i+1,i+1)
            href_list.append(ahref)
        return render(req,"classes.html",{"clases":clases,"ahref":href_list})
def classes_add(req):
    if req.method=="POST":
        names=req.POST.get("name")
        models.Classes.objects.create(name=names)
def classes_del(req):
    if req.method=="POST":
        id1=req.POST.get("id1")
        models.Classes.objects.filter(id=id1).delete()
def classes_update(req):
    if req.method=="POST":
        edit_get=req.POST.get("edit")
        edit_id_get=req.POST.get("edit_id")
        models.Classes.objects.filter(id=edit_id_get).update(name=edit_get)
def students(req):
    stu=models.Students.objects.all()
    for i in stu:
        stu_cls=models.Students.objects.get(id=i.id) #得到students表中的id
        name=stu_cls.cls.name                        #获取class表中的name值
        i.cls_name=name                              #将class表中的name值加入到i中
    return render(req,"students.html",{"stu":stu})
def students_add(req):
    if req.method=="POST":
        name=req.POST.get("name")
        username=req.POST.get("username")
        password=req.POST.get("password")
        cls_id=req.POST.get("cls_id")
        models.Students.objects.create(name=name,username=username,
                                       password=password,cls_id=cls_id)

def students_del(req):
    if req.method=="POST":
        id1=req.POST.get("id1")
        models.Students.objects.filter(id=id1).delete()
def teachers(req):
    if req.method=="GET":
        teacher_all=models.Teacher.objects.all()
        return render(req,"teachers.html",{"teacher_all":teacher_all})
def teachers_add(req):        #只是对teacher表的添加
    if req.method=="GET":
        teacher_name=req.GET.get("teacher_name")
        teacher_username=req.GET.get("teacher_username")
        teacher_pwd=req.GET.get("teacher_pwd")
        models.Teacher.objects.create(
            name=teacher_name,username=teacher_username,password=teacher_pwd,
        )
    return redirect("/teachers")
def teacher_student_add(req):
    if req.method=="POST":
        tea_name=req.POST.get("tea_name")
        if not tea_name:
            return redirect("/teacher_student_add")
        cls_id=req.POST.getlist("stu_info")
        cls_id_list=[]
        for i in cls_id:
            i=int(i)
            cls_id_list.append(i)
        models.Teacher.objects.create(name=tea_name)
        tea_id=models.Teacher.objects.get(name=tea_name).id
        tea_id1=models.Teacher.objects.get(id=tea_id)
        tea_id1.stu.add(*cls_id_list)
    cls_all=models.Classes.objects.all()
    return render(req,"teacher_student_add.html",{"cls_all":cls_all})
def teachers_check(req):
    if req.method=="POST":
        teacher_id_name=req.POST.get("teacher_id_name")  #id|name
        print(teacher_id_name)
        a=teacher_id_name.split("|")[0]   #得到id
        b=models.Teacher.objects.get(id=a)
        c=b.stu.all()                      #得到student表中所有和选中id有关的信息
        return render(req,"teachers_check.html",{"student_all":c})
    else:
        teacher_list=models.Teacher.objects.all()
        return render(req,"teachers_check.html",{"teacher_list":teacher_list})
def teacher_edit(req,edit):
    print(edit)
    # if req.method=="GET":
    #     print(req.GET.get("id"))
    return HttpResponse("ok")
def test(req):
    user=req.COOKIES.get("username")
    print(user)
    return HttpResponse("nnnn")
def jquery_cookie(req):
    return render(req,"cookie(jquery).html")

def img(req):
    if req.method=="POST":
        file=req.FILES.get("file")
        file_path=os.path.join("static","upload",file.name).replace("\\","/")
        models.File.objects.create(path=file_path)
        f=open(file_path,"wb")
        for i in file.chunks():
            f.write(i)
        f.close()
        return HttpResponse(json.dumps(file_path))
    elif req.method=="GET":
        return render(req,"img.html")
def iframe(req):
    if req.method=="POST":
        file=req.FILES.get("file")
        file_path=os.path.join("static","upload",file.name).replace("\\","/")
        models.File.objects.create(path=file_path)
        f=open(file_path,"wb")
        for i in file.chunks():
            f.write(i)
        f.close()
        return HttpResponse(json.dumps(file_path))
    elif req.method=="GET":
        return render(req,"iframe.html")

