from django.shortcuts import render , get_object_or_404

# Create your views here.
from product.models import Product
from django.core.paginator import Paginator


def product_list(requset):
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 2)
    page = requset.GET.get('page')
    product_list = paginator.get_page(page)

    context = {'product_list' : product_list}
    return render(requset , 'Product/product_list.html' , context)



def product_detail(requset , slug):
    # product_detail = Product.objects.get(PRDSlug=slug)
    product_detail = get_object_or_404(Product ,PRDSlug=slug)
    context = {'product_detail' : product_detail}
    return render(requset , 'Product/product-detail.html' , context)