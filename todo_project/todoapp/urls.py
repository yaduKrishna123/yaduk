from .import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name="demo"),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('cbvindex',views.Tasklistview.as_view(),name="cbvindex"),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name="cbvupdate"),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name="cbvdelete"),


    ]