from django.urls import path
from app import views
urlpatterns = [
   path('',views.index,name="index"),
   path('about',views.about,name="about"),
   path('view',views.view,name="view"),
   path('register',views.register,name="register"),
   path('add',views.add,name="add"),
   path('insert',views.insertData,name="insertData"),
   path('update/<id>',views.updateData,name="updataData"),
   path('delete/<id>',views.deleteData,name="deleteData"),
   
]
