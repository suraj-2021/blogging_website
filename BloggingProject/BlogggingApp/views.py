from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm


def product_list(request):
    products = Product.object.all()
    return render(request,'BloggingApp/index.html',{'products': products})

 
def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,'myapp/index2.html',{'product':product})


def edit_product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == 'POST':
       form = ProductForm(request.POST,instance = product)
       if form.is_valid():
           form.save()
           return redirect('porduct_list')
    else:
        form = ProductForm(instance = product)
    return render (request,'BloggingApp/edit.html', {'form': form})


def delete_product(request,pk):
    product = get_object_or_404(Product, pk = pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(render,'BloggingApp/delete.html',{'product': product })

def home(request):
    return HttpResponse('Hello World')




