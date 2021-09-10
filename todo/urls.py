from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.addTolist,name='addlist'),
    path('completed/<jobid>',views.jobComplete,name='completed'),
    path('deleteCompleted',views.delCompleted,name='deleteCompleted'),
    path('deleteAll',views.delAll,name='deleteAll'),
]
