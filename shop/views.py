from django.shortcuts import render
from django.http import HttpResponse
from .models import product,Contact,Orders,OrderUpdate
from math import ceil
import json
from rest_framework.views import APIView
from rest_framework.response import Response




# Create your views here.
def index(request):
    allprods=[]
    catprods=product.objects.values('category')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nSlide= n//4+ ceil((n/4)-(n//4))
        allprods.append([prod,nSlide,range(1,nSlide)])

    params={'allprods':allprods}
    return render(request,'shop/index.html',params)


def about(request):
    return render(request,'shop/about.html')



# class Contact(APIView):
#     def get(self,request):
#         # request.query_params for get api
#         # request.data for post
#         params = Orders.objects.filter(order_id =15).values()
#         return Response({"data": params})




def contact(request):
    if request.method=="POST":
        thank = False
        if( request.POST.get('name') and request.POST.get('desc') and request.POST.get('phone') and request.POST.get('email')):
            name=request.POST.get('name','')
            desc=request.POST.get('desc','')
            phone=request.POST.get('phone','')
            email=request.POST.get('email','')
            contact=Contact(name=name, desc=desc, email=email, phone=phone)
            contact.save()

            thank = True
        return render(request,'shop/contact.html', {'thank': thank})
    else:
        return render(request,'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid',"")
        email = request.POST.get('email',"")
        
        
        try:
            order = Orders.objects.filter(order_id = orderid , email = email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id = orderid)
                updates =[]
                for item in update:
                    updates.append({'text':item.update_desc , 'time':item.timestamp})
                    response = json.dumps([updates, order[0].items_json] , default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')


    return render(request,'shop/tracker.html')



def search(request):
    return render(request,'shop/search.html')

def productview(request,myid):
    prod=product.objects.filter(id=myid)
    return render(request,'shop/productview.html',{'product':prod[0]})

def checkout(request):
    # b = Orders.objects.filter(order_id =15).values()
    # b = Orders.objects.all().values()
    # mydata = Orders.objects.filter(order_id =16).values()
    # info = { 'order' : mydata }


    # print(b[0].__dict__)
    # for i in  b:
    #     print(i.name)
    if request.method == 'POST':
        order=Orders()
        order.items_json = request.POST.get('itemjson','')
        order.amount = request.POST.get('amount','')
        order.name = request.POST.get('name','')
        order.email = request.POST.get('email','')
        order.address = request.POST.get('address','') +" , "+ request.POST.get('address2','')
        order.phone = request.POST.get('phone','')
        order.city = request.POST.get('city','')
        order.state = request.POST.get('state','')
        order.zip_code = request.POST.get('zip','')
        order.save()

        update = OrderUpdate(order_id = order.order_id , update_desc = "The order has been placed succesfully.")
        update.save()
  

        thank=True
        id=order.order_id
        return render(request,'shop/checkout.html',{'thank': thank , 'id':id})
    
    return render(request,'shop/checkout.html' )
