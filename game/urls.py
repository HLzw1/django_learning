from django.urls import path
from game.views import index, play, indexyyf, indexzq, indexlwx, indexlsy

urlpatterns = [
    path("", index,name = "index"),
    path("classmates/yyfsb", indexyyf, name = "index1"),
    path("classmates/zqsb", indexzq, name = "index2"),
    path("classmates/lwxsb", indexlwx, name = "index3"),
    path("classmates/lsysb", indexlsy, name = "index4"),
    path("play/", play, name = "play"),
]
