from django.urls import path
from . import views

# view에 있는 index.html을 적용
urlpatterns = [
    #/번호 입력하면 해당 페이지를 출력
    path('<int:pk>/',views.single_post_page),
    path('',views.index)
]
