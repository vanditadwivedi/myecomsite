from operator import truediv
from django.shortcuts import render
from django.http import HttpResponse
from .models import Orders, product,Contact,Orders,OrderUpdate
from math import ceil
import json
# Create your views here.
def index(request):
    #products = product.objects.all()
  #  n = len(products)
   # print(products)
    #n_slides = n//4 + ceil((n/4) - (n//4))
   # param = {'no_of_slides': n_slides, 'range': range(1, n_slides), 'product': products}
   # allProds=[[products, range(1, n_slides), n_slides], [products, range(1,n_slides), n_slides]]
    allProds=[]
    catProds = product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        n_slides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, n_slides), n_slides])
    param = {'allProds': allProds}
    return render(request, 'shop/index.html', param)
def searchMatch(querry,item):
    if querry in item.desc.lower() or querry in item.product_name.lower() or querry in item.category.lower():
        return True
    else:
        return False

def search(request):
    querry=request.GET.get('search')
    allProds=[]
    catProds = product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prodtemp = product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(querry,item)]
        n = len(prod)
        n_slides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!=0:
            allProds.append([prod, range(1, n_slides), n_slides])
    param = {'allProds': allProds,'msg':""}
    print(allProds)
    if len(allProds)==0:
        param= {'msg':"please try to enter relevant keywords"}
    return render(request, 'shop/search.html',param)


def about(request):
    return render(request, 'shop/about.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')
def contact(request):
    if request.method=='POST':
        #thank=False
        print(request)
        name=request.POST.get("name","")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        desc = request.POST.get("desc", "")
        print(name,email,phone,desc)
        contact= Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        #thank=True
    return render(request,'shop/contact.html')
def checkout(request):
     if request.method=='POST':
        #print(request)
        name = request.POST.get("name", "")
        print(name)
        email = request.POST.get("email", "")
        address = request.POST.get("address1", "") +""+request.POST.get("address2", "")
        state= request.POST.get("state", "")
        city = request.POST.get("city", "")
        zip = request.POST.get("zip", "")
        items_jason=request.POST.get("items_jason","")
        order= Orders(name=name,email=email,address=address,state=state,city=city,zip=zip,items_jason=items_jason)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thanks=True
        id=order.order_id
        return render(request, 'shop/checkout.html',{'thanks':thanks,'id':id})
     return render(request, 'shop/checkout.html')
    #eturn HttpResponse('HELLO')
def prodview(request,myid):
    #fetching product using id
    produc = product.objects.filter(id=myid)
    return render(request, 'shop/prodview.html', {'product': produc[0]})

