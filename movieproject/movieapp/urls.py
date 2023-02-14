from django.urls import path
from . import views

app_name='movieapp'
urlpatterns = [

    path('',views.demo,name='demo'),


    path('movie/<int:movieid>/',views.detail,name='detail'),
    path('add/',views.addmov,name='addmov'),
    path('edit/<int:id>/',views.update,name='update'),
path('del/<int:id>/',views.delete,name='delete')

    ]