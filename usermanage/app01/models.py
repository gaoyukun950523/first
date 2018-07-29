from django.db import models

# Create your models here.
class Classes(models.Model):
    name=models.CharField(max_length=32)      #哪个班级
class Students(models.Model):
    name=models.CharField(max_length=32)      #学生名字
    username=models.CharField(max_length=32)  #用户名
    password=models.CharField(max_length=32)  #密码
    cls=models.ForeignKey("Classes",on_delete=models.CASCADE)     #所在班级
class Teacher(models.Model):
    name=models.CharField(max_length=32)    #教师名字
    username=models.CharField(max_length=32)  #用户名
    password=models.CharField(max_length=32)  #密码
    stu=models.ManyToManyField("Students") #老师对学生（多对多）
    def __str__(self):
        return self.name
class File(models.Model):
    path=models.CharField(max_length=128)
