"""usermanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app01 import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),      #登陆界面
    path('login1/',views.Login.as_view()),
    path('index/',views.index),      #后台界面
    path('test/',views.test),        #测试
    path('jquery_cookie',views.jquery_cookie),  #jquery_cookie设置
    path('classes',views.classes),
    path('students',views.students),
    path('teachers',views.teachers),
    path('teachers_add',views.teachers_add),
    path('teacher_student_add',views.teacher_student_add),
    re_path('teacher_edit-(\d+)',views.teacher_edit),
    path('teachers_check',views.teachers_check),
    path('classes_add',views.classes_add),
    path('classes_del',views.classes_del),
    path('classes_update',views.classes_update),
    path('students_add',views.students_add),
    path('students_del',views.students_del),
    path('img/',views.img),
    path('iframe',views.iframe),
]
urlpatterns += staticfiles_urlpatterns()