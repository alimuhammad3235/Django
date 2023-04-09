from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("see/",views.ListproductAPIView.as_view(),name="todo_list"),
    path("create/", views.CreateproductAPIView.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateproductAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteproductAPIView.as_view(),name="delete_todo")

]