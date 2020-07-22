from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('update/<str:pk>/',views.updatelist,name='update'),
    path('delete/<str:pk>/',views.deletetask,name='delete'),
]