from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request, numero1, numero2):
    resultado = numero1 + numero2

    return HttpResponse('<h1>A soma {} + {} = {}.</h1>'.format(numero1, numero2, resultado))

