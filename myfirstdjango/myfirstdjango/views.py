from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Добро пожаловать на главную страницу!</h1><p>Выберите страницу: /data/ или /test/.</p>")