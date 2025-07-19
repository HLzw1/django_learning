from django.http import HttpResponse

def index(resquest):
    line1 = '<h1 style="text-align:center">叶研凤是个杀软</h1>'
    line2 = '<hr>'
    line4 = '<a href="play/">进入游戏页面</a>'
    line3 = '<img src="" width=2000>'
    return HttpResponse(line1 +line2 + line3)

def play(resquest):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line2 = '<a href="/yyfsb">回到菜单</a>'
    line3 = '<hr>'
    return HttpResponse(line1 + line2 + line3)
