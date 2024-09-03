from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Djando - Coder")