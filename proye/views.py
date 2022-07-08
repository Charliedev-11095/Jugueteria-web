from django.shortcuts import render

def proyecto(request):    
    return render(request,"proye/index.html")

def producto(request):
    return render(request,"proye/producto.html")

def filtrado(request):
    return render(request,"proye/filtrado.html")

def contacto(request):
    return render(request,"proye/contacto.html")