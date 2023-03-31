import datetime
from django.utils import timezone
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Merchants,Product,Costomer,Order,Status,Admin,Help,Delivery_status
from .forms import MerchantReg,Product_items,Costomer_Reg,Order_details,Help_form


def home(request):
    if 'user' in request.session:
        return redirect('Merchant_home')
    if 'costomer' in request.session:
        return redirect('Costomer_home')
    if 'admn' in request.session:
        return redirect('admin_home')
    else:
        return render(request,'home.html')

#user login

def MerchantLogin(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        user = Merchants.objects.filter(username=username, password=password)
        if user:
            request.session['user'] = username
            return redirect('Merchant_home')
            #return render(request,"merchanthome.html",{'username':username})
        else:
            return HttpResponse("enter valid data")
    return render(request,'merchant_login1.html')
#merchant signup

def Merchantsignup(request):
    form = MerchantReg()
    if request.method == 'POST':
        form=MerchantReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('merchantlogin')
    return render(request,'merchantsignup.html',{'form':form})

#merchant login home

def Merchant_home(request):
    if 'user' in request.session:
        username=request.session['user']
        products=Product.objects.filter(merchant_username=username)
        return render(request,'merchanthome.html',{'objs':products,'username':username})
    return render(request,'home.html')

def CreateProduct(request):
    form = Product_items()
    if request.method=='POST':
        username=request.session['user']
        form=Product_items(request.POST,request.FILES)
        g=form.is_valid()
        print(g)
        if form.is_valid():
            data=form.save(commit=True)
            print(form.data)
            data.merchant_username=username
            data = form.save()
            # datas=form.save(commit=False)
            # datas.images=request.FILES['image']
            # datas.username=username
            # datas.save()
            # print(datas.username)
            return redirect('Merchant_home')
        return HttpResponse("fail")
    return render(request,'product_create.html',{'form':form})

#
#products details view

def ProductDetails(request,id):

    c=Product.objects.get(pk=id)
    return render(request,'product_details.html',{'context_object':c})

#update products

def Product_update(request,id):
    obj=Product.objects.get(id=id)
    form=Product_items(instance=obj)
    if request.method=="POST":
        form=Product_items(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return ('Merchant_home')
    return render(request,'update_product.html',{'form':form})
#product delete
def Product_delete(request,id):
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect('Merchant_home')

#merchant logout
def LogoutMerchant(request):
    try:
        del request.session['user']
    except:
        return redirect('Merchant_home')
    return redirect('home')


#merchant profile
def merchant_profile_view(request):
    username=request.session['user']
    profile=Merchants.objects.get(username=username)
    if profile:
        return render(request,'merchant_profile.html',{'obj':profile})
    return HttpResponse("user not found")

#merchant profile update

def Merchant_profile_update(request,pk):
    obj = Merchants.objects.get(pk=pk)
    print(obj)
    form =MerchantReg(instance=obj)
    if request.method == "POST":
        form = MerchantReg(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Merchant_home')
    return render(request, 'merchant_profile_update.html', {'form': form})

#costomer signup

def Costomer_signup(request):
    form =Costomer_Reg()
    if request.method == 'POST':
        form = Costomer_Reg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CostomerLogin')
    return render(request, 'costomer_signup.html', {'form': form})

#def costomer login

def CostomerLogin(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        user = Costomer.objects.filter(costomer_username=username, password=password)
        if user:
            request.session['costomer'] = username
            return redirect('Costomer_home')
            #return render(request,"merchanthome.html",{'username':username})
        else:
            return HttpResponse("enter valid data")
    return render(request,'costomer_login.html')

# costomer home page

def Costomer_home(request):
    if 'costomer' in request.session:
        username=request.session['costomer']
        query=request.GET.get("qry")
        products = Product.objects.all()
        if query is not None:
            products=Product.objects.filter(product_name__icontains=query)
            return render(request,'costomer_home.html',{'objs':products,'username':username})
        else:
            return render(request, 'costomer_home.html', {'objs': products, 'username': username})
    return render(request,'home.html')

#product details for booking

def Product_merchant_Details(request,id):
    product=Product.objects.get(id=id)
    print(product)
    username=Product.objects.filter(id=id).values_list('merchant_username',flat=True)
    print(username)
    m=Merchants.objects.get(username__in=username)
    print(m)
    return render(request,'Product_merchant_Details.html',{'context_object':product,'obj':m})

def delivery_details(request,id,pk):
    form=Order_details()
    costomer_username = request.session['costomer']
    print(costomer_username)
    product = Product.objects.get(id=id)
    costomer = Costomer.objects.get(costomer_username=costomer_username)
    merchant = Merchants.objects.get(merchantid=pk)
    print(merchant)
    merchant_username = merchant.username
    price = product.price
    product_name = product.product_name
    status=False
    if request.method == "POST":
        form = Order_details(request.POST)
        print(form.data)
        g=form.is_valid()
        print(g)
        if form.is_valid():
            data=form.save(commit=False)
            data.costomer_username=costomer.costomer_username
            print(data.costomer_username)
            data.merchant_username =merchant_username
            data.price = price
            data.product_name = product_name
            data.status = False
            data.total_amount=price * data.qty
            print(form.data)
            data.save()
            return render(request,'order_success.html')
        else:
            return HttpResponse("order fail")
    return render(request,'order_details1.html',{'form':form})

#cotomer oder list

def Costomer_orders(request):
    username=request.session['costomer']
    print(username)
    lists=Order.objects.filter(costomer_username=username,status=False).values()
    print(lists)
    if lists:
        return render(request,'costomer_orders.html',{'lists':lists})
    return render(request,'no_order_costomer.html')

def Costmer_order_cancel(request,id):
    obj = Order.objects.get(id=id)
    print(obj)
    obj.delete()
    return redirect('Costomer_orders')

#costomer profile update

def Costomer_update(request,pk):
    username = request.session['costomer']
    obj=Costomer.objects.get(pk=pk)
    print(obj)
    form=Costomer_Reg(instance=obj)
    if request.method=="POST":
        form=Costomer_Reg(request.POST or None, instance=obj)
        print(form.data)
        g=form.is_valid()
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return redirect('Costomer_home')
    return render(request,'costomer_profile_update.html',{'form':form})

#costomer profile
def costomer_profile_view(request):
    username=request.session['costomer']
    profile=Costomer.objects.get(costomer_username=username)
    if profile:
        return render(request,'costomer_profile_view.html',{'obj':profile})
    return HttpResponse("user not found")

#costomer logout
def LogoutCostomer(request):
    try:
        del request.session['costomer']
    except:
        return redirect('Merchant_home')
    return redirect('home')

def Aboutas(request):
    return render(request,'about_as.html')

def Merchant_orders(request):
    username=request.session['user']
    # print(username)
    lists=Order.objects.filter(merchant_username=username,status=False).values()
    print(lists)
    if lists:
        return render(request,'merchant_order.html',{'lists':lists})
    return render(request,'no_orders.html')

def manage_order(request):
    username = request.session['user']
    print(username)
    lists = Order.objects.filter(merchant_username=username,status=False).values()
    # products=lists.objects.filter(status=False)
    print(lists)
    if lists:
        return render(request, 'manage_order.html', {'lists': lists})
    return render(request, 'no_orders.html')

def delivered(request,id):
    list=Order.objects.get(id=id)
    print(list)
    if list:
        list.status=True
        list.save(update_fields=['status'])
        return redirect('Merchant_home')
    return HttpResponse("error")

#admin home

def admin_home(request):
    if 'admn' in request.session:
        username = request.session['admn']
        return render(request, 'admin_home.html', {'username': username})
    return render(request, 'home.html')

def admintLogin(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        admn = Admin.objects.filter(admn=username, password=password)
        if admn:
            request.session['admn'] = username
            return redirect('admin_home')
            #return render(request,"merchanthome.html",{'username':username})
        else:
            return HttpResponse("enter valid data")
    return render(request,'admin_login.html')

# all porducts list form admin

def Poducts_list(request):
    # products=Product.objects.all()
    # print(products)
    # if products:
    #     return (request,'product_list.html',{'obj':products})
    # return HttpResponse("no list avilable")
    if 'admn' in request.session:
        username=request.session['admn']
        products=Product.objects.all()
        print(products)
        return render(request,'product_list.html',{'objs':products,'username':username})
    return render(request,'home.html')

def admin_product_Details(request,id):
    product=Product.objects.get(id=id)
    print(product)
    username=Product.objects.filter(id=id).values_list('merchant_username',flat=True)
    print(username)
    m=Merchants.objects.get(username__in=username)
    print(m)
    return render(request,'admin_product_details.html',{'context_object':product,'obj':m})

def delete_admn_product(request,id):
    obj=Product.objects.get(id=id)
    obj.delete()
    return redirect('Poducts_list')


#merchant lists
def merchant_list(request):
    if 'admn' in request.session:
        merchants = Merchants.objects.all()
        print(merchants)
        return render(request, 'merchant_lists.html', {'objs': merchants})
    return render(request, 'home.html')

#costomer details for admin

def costomer_list(request):
    if 'admn' in request.session:
        costomer = Costomer.objects.all()
        print(costomer)
        return render(request, 'costomer_list.html', {'objs': costomer})
    return render(request, 'home.html')
def costomer_delete(request,pk):
    obj = Costomer.objects.get(pk=pk)
    obj.delete()
    return redirect('costomer_list')

def merchant_delete(request,pk):
    obj = Merchants.objects.get(pk=pk)
    obj.delete()
    return redirect('merchant_list')


#all oder list for admin

def order_list(request):
    if 'admn' in request.session:
        order = Order.objects.all()
        print(order)
        return render(request, 'order_lists.html', {'objs': order})
    return render(request, 'home.html')

def Helpsend(request):
    form=Help_form()
    if request.method=="POST":
        form=Help_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("sended successfully")
    return render(request, 'costomer_help.html', {'form': form})

def Helpview(request):
    q=Help.objects.all()
    return render(request,'admin_help.html',{'q':q})

def Logoutadmin(request):
    try:
        del request.session['admn']
    except:
        return redirect('admin_home')
    return redirect('home')

def delivery_status_update(request,id):
    order = Order.objects.get(id=id)
    o_id=id
    if request.method=='POST':
        d_id=request.POST.get('order_id')
        d_status=request.POST.get('delivery_status')
        d_date=request.POST.get('delivery_date')
        delivery=Delivery_status(order_id=d_id,delivery_status=d_status,delivery_date=d_date)
        delivery.save()
        order.d_status = d_status
        order.d_status_time=d_date
        order.save(update_fields=['d_status','d_status_time'])
        # order.save()
        return redirect('Merchant_orders')
    return render(request,'delivery_update.html',{'id':o_id})
# Create your views here.
def order_track(request,id):
    user=request.session['costomer']
    # booking=Booking.objects.filter(username=user,status=False).first()
    # count=booking.count()
    # print(count)
    # print(booking[0])
    # booking=booking[0]
    # booking=Booking.order_by(username=user).first()
    order=Order.objects.filter(costomer_username=user).first()
    # order=Order.order_by(user_username=user).first()
    if order:
        oid=id
        # id=booking.id
        print(oid)
        # print(id)
        d_s=order.d_status
        date = datetime.date.today()
        if d_s=='Order_collected':
            return render(request, 'order_collected.html', {'date': date,'oid':oid})
        elif d_s=='Order_arrived':
            return render(request, 'order_arrived.html', {'date': date,'oid':oid})
        elif d_s == 'Order_en_route':
            return render(request, 'order_enroute.html', {'date': date,'oid':oid})
        else:
            return render(request,'order_placed.html',{'date':date,'oid':oid})
    else:
        return HttpResponse("you dont have any orders")