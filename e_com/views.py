from django.shortcuts import render,redirect                      #to return html file as response
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import *
from .forms import RegisterForm,ProductDetailForm
from django.views.generic import TemplateView 
from django.http import JsonResponse
import json
#now we create method for our pipeline/urls here 

def item_view(request):
    return render(request,'itemPage.html')

def homepage(request):                             #retuns the page as response
    products=ProductDetail.objects.values("title","price","summary","sellerlocation","quantity","imagefile")
    contex={
        'matched_product':products
    }
    
    u_email=request.POST.get('email')
    psw=request.POST.get('psw')
    u_login=Register.objects.values('email','password')
    
    user_info={}
    for name in u_login:
        user_info[name["email"]]=name["password"]
    if  u_email in user_info and user_info[u_email]==psw:
        contex["user_login_email"]=u_email
        homepage.valid_email=u_email
        
        return redirect('/userlogin/',u_email)
        
    return render(request,'index.html',contex)

def login_validation(request):
    #login to the system from here
    homepage(request)
    products=ProductDetail.objects.values("title","price","summary","sellerlocation","quantity","imagefile")
    contex={
        'matched_product':products,
        "user_login_email":homepage.valid_email
    }
    
    return render(request,"afterlogin.html",contex)



class loginproductView(TemplateView):
    template_name='afterloginshop.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {"qs": CompanyProductDetail.objects.all()}
        return context




def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}

    products = CompanyProductDetail.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'product.html', context)



def register_user(request):
    form=RegisterForm()                             #retuns the page as response
    if request.method=="POST":
        form=RegisterForm(request.POST or None)
    contex={
        "form":form,
        
    }
    if form.is_valid():
        form.save()
        return redirect('/register/')

    contex={
        "form":form,
        
    }
    return render(request,'register.html',contex)


def product_detail(request):
    form=ProductDetailForm()                             #retuns the page as response
    lastimage= ProductDetail.objects.last()
    #imagefile= lastimage.imagefile
    if request.method=="POST":
        form=ProductDetailForm(request.POST or None, request.FILES or None)
    contex={
        "form":form,
        
    }
    if form.is_valid():
        form.save()
        return redirect('/supplierproductdetail/')
    contex={
        "form":form,
    }
    return render(request,'supplierproductdetail.html',contex)

def search(request):
    matched_product=[]
    products=[]
    u_products=ProductDetail.objects.values("title","price","summary","sellerlocation","quantity","imagefile")
    c_products=CompanyProductDetail.objects.values("title","price","summary","sellerlocation","quantity","imagefile")
    for u_product in u_products:
        products.append(u_product)
    for c_product in c_products:
        products.append(c_product)
    search_=request.GET.get('search')
    for product in products:
        if search_.lower() in product['title'].lower() or search_.lower() in product['summary'].lower():
            matched_product.append(product)
    contex={
        'matched_product':matched_product
    }
    return render(request,"search.html",contex)
#after user is logged in it will implement search
def login_search(request):
    matched_product=[]
    products=[]
    u_products=ProductDetail.objects.values("title","price","summary","sellerlocation","quantity","imagefile")
    c_products=CompanyProductDetail.objects.values("title","price","summary","sellerlocation","quantity","imagefile")
    for u_product in u_products:
        products.append(u_product)
    for c_product in c_products:
        products.append(c_product)
    search_=request.GET.get('search')
    for product in products:
        if search_.lower() in product['title'].lower() or search_.lower() in product['summary'].lower():
            matched_product.append(product)
    contex={
        'matched_product':matched_product
    }
    return render(request,"afterloginsearch.html",contex)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}

    products = CompanyProductDetail.objects.all()
    context = {'products':products, 'cartItems':cartItems,'items':items,'order':order}
    return render(request, 'cart.html', context)

def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
    
    products = CompanyProductDetail.objects.all()
    context = {'items':items,'order':order,'products':products, 'cartItems':cartItems}
    return render(request,"checkout.html",context)    

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = CompanyProductDetail.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)