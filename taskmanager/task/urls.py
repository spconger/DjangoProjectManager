from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    path('newproject', views.newproject, name='newproject'),
    path('worktimes/', views.worktimes, name='worktimes'),
    path('logs/', views.logs, name='logs'),
]