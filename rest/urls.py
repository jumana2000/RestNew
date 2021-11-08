"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from restapp.views import TaskViewset,CreateuserView,UpdateTaskAPIView,DestroyTaskAPIView
from restapp import views

router=routers.SimpleRouter()
router.register('task',views.TaskViewset)
router.register('completed_task',views.CompletedTaskViewset)
router.register('due_task',views.DueTaskViewset)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('register/',views.CreateuserView.as_view(),name='user'),
    path('api_auth/',include('rest_framework.urls')),
    # path("task/<int:pk>", views.RetrieveTaskAPIView.as_view()),
    path("task/<int:pk>", views.UpdateTaskAPIView.as_view()),
    path("task/delete/<int:pk>", views.DestroyTaskAPIView.as_view()),
    path('',include(router.urls)),

]
