from django.urls import path
from . import views
urlpatterns=[
    path('',views.item, name='item'),
    path('<int:pk>/',views.detail, name='detail'),
    
]    