from django.http import HttpResponse

def index(resquest):
    line1 = '<h1 style="text-align:center">游戏页面</h1>'
    line2 = '<hr>'
    line4 = '<a href="play/">进入游戏页面</a>'
    line3 = '<img src="https://picx.zhimg.com/80/v2-c0ba9958a5bdc140c1f5f2af325cfbda_720w.png" width=1000 style="display: block; margin: 0 auto;">'
    return HttpResponse(line1 +line2)

def play(resquest):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line2 = '<a href="/yyfsb">回到菜单</a>'
    line3 = '<hr>'
    return HttpResponse(line1 + line2 + line3)

def indexyyf(resquest):
    line1 = '<h1 style="text-align:center">叶妍凤-"杀软"</h1>'
    line2 = '<hr>'
    line3 = '<img src="https://picx.zhimg.com/80/v2-c0ba9958a5bdc140c1f5f2af325cfbda_720w.png" width=1000 style="display: block; margin: 0 auto;">'
    return HttpResponse(line1 + line2 + line3)

def indexzq(resquest):
    line1 = '<h1 style="text-align:center">周虔-"数学天才"</h1>'
    line2 = '<hr>'
    line3 = '<img src="https://pica.zhimg.com/80/v2-bc1e7d66505170f2c294d1ba78ef4d0c_720w.jpeg" width=1000 style="display: block; margin: 0 auto;">'
    return HttpResponse(line1 + line2 + line3)

def indexlwx(resquest):
    line1 = '<h1 style="text-align:center">刘卫轩-"传奇插班生"</h1>'
    line2 = '<hr>'
    line3 = '<img src="https://pic1.zhimg.com/80/v2-7d36be99ca9546f777a9363c3206b661_720w.jpeg" width=1000 style="display: block; margin: 0 auto;">'
    return HttpResponse(line1 + line2 + line3)

def indexlsy(resquest):
    line1 = '<h1 style="text-align:center">牛逼廖思懿</h1>'
    line2 = '<hr>'
    line3 = '<img src="" width=1000 style="display: block; margin: 0 auto;">'
    line3 = '<img src="https://picx.zhimg.com/80/v2-29ecb94a1fa31b540f68a0ebeb4d8b5b_720w.jpeg" width=1000 style="display: block; margin: 0 auto;">'
    return HttpResponse(line1 + line2 + line3) 
