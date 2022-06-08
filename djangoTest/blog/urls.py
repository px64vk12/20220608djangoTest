from django.urls import path
from . import views

# view에 있는 index.html을 적용
urlpatterns = [
    path('',views.index)
]
