from django.urls import path
from dinner import views
urlpatterns=[
  path('info',views.func,name='home'),
  path('and',views.fun1,name='item'),
]