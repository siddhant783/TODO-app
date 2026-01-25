from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.landing, name="landing"),
    path('home/', views.home, name="home"),
    path('register/',views.register_views,name="register"),
    path('login/',views.login_views,name="login"),
    path('logout/',views.logout_views,name="logout"),
    path('delete/<int:id>/',views.delete_task,name="delete"),
    path('update/<int:id>/',views.update_task,name="update"),
    path('complete/<int:id>/', views.complete_task, name="complete"),

]