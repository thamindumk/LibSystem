from django.urls import path
from . import views

urlpatterns = [
    path('',views.bookList,name="home"),
    path('add/',views.addBook,name = "add"),
    path('delete/<int:id>/',views.delete , name= "delete"),
    path('search/',views.search, name = "search")
]
