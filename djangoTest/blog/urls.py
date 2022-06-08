from django.urls import path

if 0:
    from . import viewsFBV

    # view에 있는 index.html을 적용
    urlpatterns = [
        #/번호 입력하면 해당 페이지를 출력
        path('<int:pk>/',viewsFBV.single_post_page),
        path('',viewsFBV.index)
    ]

else:
    from . import viewsCBV

    # view에 있는 index.html을 적용
    urlpatterns = [
        #/번호 입력하면 해당 페이지를 출력
        path('<int:pk>/',viewsCBV.PostDetail.as_view()),
        path('', viewsCBV.PostList.as_view())
    ]