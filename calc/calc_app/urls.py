from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name="add"),
    path('addition', views.addition, name="addition"),
    path('sub', views.sub, name="sub"),
    path('subtraction', views.subtraction, name="subtraction"),
    path('mul', views.mul, name="mul"),
    path('multiplication', views.multiplication, name="multiplication"),
    path('div', views.div, name="div"),
    path('division', views.division, name="division"),
 ] 