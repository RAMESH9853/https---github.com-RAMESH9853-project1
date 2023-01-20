from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductMainModel,productColourModel,productImageModel

def allProduct(request):
    data1 = ProductMainModel.objects.all()
    data2 = productColourModel.objects.all()
    data3 = productImageModel.objects.all()
    data = {'table1':list(data1.values('Title','Description','Price','Size','Quality')),'table2':list(data2.values('Product','Colour')),'table3':list(data3.values('Product','Image'))}
    return HttpResponse (data)


def productid(request):
    data1 = ProductMainModel.objects.all()
    data2 = productColourModel.objects.all()
    data3 = productImageModel.objects.all()
    data = {'table1':list(data1.values('id','Title','Description','Price','Size','Quality')),'table2':list(data2.values('id','Product','Colour')),'table3':list(data3.values('id','Product','Image'))}
    return HttpResponse (data)
