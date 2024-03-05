from django.shortcuts import render,redirect
from .models import *
from .forms import YourModelSearchForm
from django.contrib import messages
from django.contrib.auth.models import *
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate
from django.http import JsonResponse,HttpResponse
import random,re
# import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
# Create your views here.
def search_view(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        usr=User.objects.filter(id=val).first()
        p=profilepic.objects.filter(user=usr).first()

        cnt=c.count()
        wcnt=w.count()
        if r.method == 'POST':
            search_term = r.POST.get('sear')
            obj = productdet.objects.filter(name__icontains=search_term)
        return render(r,'s.html',{'obj':obj,'cnt':cnt,'wcnt':wcnt,'usr':usr,'p':p})
    else:
        if r.method == 'POST':
            search_term = r.POST.get('sear')
            obj = productdet.objects.filter(name__icontains=search_term)
            return render(r, 's.html', {'obj': obj})
        return redirect(index)
def index(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        c=mycart.objects.filter(usr=val).all()
        w=wish.objects.filter(usr=val).all()
        usr=User.objects.filter(id=val).first()
        p=profilepic.objects.filter(user=usr).first()
        cnt=c.count()
        wcnt=w.count()
        obj=productdet.objects.all()
        l=[]
        for i in obj:
            if len(l)<3:
                l.append(i)
            else:
                pass
        return render(r,'index.html',{'l':l,'cnt':cnt,'wcnt':wcnt,'usr':usr,'p':p})
    else:
        obj=productdet.objects.all()
        l=[]
        for i in obj:
            if i.category=='a':
                if len(l)<=6:
                    l.append(i)
                else:
                    pass
        return render(r,'index.html',{'l':l})
def base(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        usr=User.objects.filter(id=val).first()
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        p=profilepic.objects.filter(user=usr).first()
        cnt=c.count()
        wcnt=w.count()
        return render(r,'base.html',{'cnt':cnt,'wcnt':wcnt,'usr':usr,'p':p})
    else:
        return render(r,'base.html')
def wishlist(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        usr=User.objects.filter(id=val).first()
        p=profilepic.objects.filter(user=usr).first()
        cnt=c.count()
        wcnt=w.count()
        ca=[]
        for i in c:
            ca.append(i.products_id)
        cl={}
        for i in w:
            cl[i.products]=[i.id]
        return render(r,'wishlist.html',{'cnt':cnt,'wcnt':wcnt,'usr':usr,'w':w,'cl':cl,'p':p,'ca':ca})
    return redirect(login)
def addwish(r,wal=0):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        c=wish.objects.filter(usr=val).all()
        if r.method=='POST':
            p=productdet.objects.filter(id=wal).first()
            usr=User.objects.filter(id=val).first()
            if c:
                val=wish.objects.create(usr=usr,products=p)
                val.save()
                return redirect(shop)
            else:
                val=wish.objects.create(usr=usr,products=p)
                val.save()
                return redirect(shop)
    return redirect(login)
def delwish(r,de):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        c=wish.objects.get(id=de)
        c.delete()
        return redirect(shop)
def glass(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        usr=User.objects.filter(id=val).first()
        p=profilepic.objects.filter(user=usr).first()
        cnt=c.count()
        wcnt=w.count()
        return render(r,'glass.html',{'cnt':cnt,'wcnt':wcnt,'usr':usr,'p':p})
    else:
        return render(r,'glass.html')
def shop(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        usr=User.objects.filter(id=val).first()
        p=profilepic.objects.filter(user=usr).first()
        ca=[]
        for i in c:
            ca.append(i.products_id)
        cnt=c.count()
        wcnt=w.count()
        obj=productdet.objects.all()
        return render(r,'shop.html',{'obj':obj,'cnt':cnt,'wcnt':wcnt,'usr':usr,'p':p,'ca':ca})
    else:
        obj=productdet.objects.all()
        return render(r,'shop.html',{'obj':obj})
def contact(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        usr=User.objects.filter(id=val).first()
        p=profilepic.objects.filter(user=usr).first()
        p=profilepic.objects.filter(user=usr).first()
        cnt=c.count()
        wcnt=w.count()
        if r.method=='POST':
            n=r.POST.get('name')
            m=r.POST.get('mob')
            e=r.POST.get('email')
            me=r.POST.get('message')
            l=msg.objects.create(name=n,mobile=m,email=e,message=me)
            l.save()
            return redirect(contact)
        return render(r,'contact.html',{'cnt':cnt,'wcnt':wcnt,'usr':usr,'p':p})
    else:
        if r.method=='POST':
            n=r.POST.get('name')
            m=r.POST.get('mob')
            e=r.POST.get('email')
            me=r.POST.get('message')
            l=msg.objects.create(name=n,mobile=m,email=e,message=me)
            l.save()
        return render(r,'contact.html')
def prodet(r,wal):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(usr=val).all()
        
        l=productdet.objects.filter(id=wal).first()
        usr=User.objects.filter(id=val).first()
        p=profilepic.objects.filter(user=usr).first()
        c=mycart.objects.filter(usr=val).all()
        ca=[]
        for i in c:
            ca.append(i.products_id)
        wa=[]
        for i in w:
            wa.append(i.products_id)
        cnt=c.count()
        wcnt=w.count()
        return render(r,'prodet.html',{'cnt':cnt,'wcnt':wcnt,'l':l,'usr':usr,'p':p,'ca':ca,'wa':wa})
    else:
        l=productdet.objects.filter(id=wal).first()
        return render(r,'prodet.html',{'l':l})
def about(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        usr=User.objects.filter(id=val).first()
        p=profilepic.objects.filter(user=usr).first()
        cnt=c.count()
        wcnt=w.count()
        return render(r,'about.html',{'cnt':cnt,'wcnt':wcnt,'usr':usr,'p':p})
    else:
        return render(r,'about.html')
def cart(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        usr=User.objects.filter(id=val).first()
        p=profilepic.objects.filter(user=usr).first()
        cnt=c.count()
        wcnt=w.count()
        cl={}
        t=0
        for i in c:
            # p=productdet.objects.filter(id=i.products).first()
            cl[i.products]=[i.quantity,i.id,i.products.discount*i.quantity]
            t=t+(i.products.discount*i.quantity)
        
        return render(r,'cart.html',{'usr':usr,'cl':cl,'cnt':cnt,'wcnt':wcnt,'t':t,'p':p})
    return redirect(login)
def addcart(r,wal=0):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        c=mycart.objects.filter(usr=val).all()
        if r.method=='POST':
            
            p=productdet.objects.filter(id=wal).first()
            usr=User.objects.filter(id=val).first()
            if c:
                f=0
                for i in c:
                    if i.products==p :
                        f=1
                        i.quantity=i.quantity + 1
                        i.save()
                        return redirect(shop)
                if f==0:
                    val=mycart.objects.create(usr=usr,products=p,quantity=1)
                    val.save()
                    return redirect(shop)
            else:
                val=mycart.objects.create(usr=usr,products=p,quantity=1)
                val.save()
                return redirect(shop)
    return redirect(login)
def minuscart(r,de):
    c=mycart.objects.get(id=de)
    if c.quantity>1:
        c.quantity=c.quantity-1
        c.save()
    else:
        c.delete()
    return redirect(cart)
def pluscart(r,de):
    c=mycart.objects.get(id=de)
    c.quantity=c.quantity+1
    c.save()
    return redirect(cart)
def delcart(r,de):
    c=mycart.objects.get(id=de)
    c.delete()
    return redirect(cart)
def login(r):
    if r.method=='POST':
        u=r.POST.get('username')
        p=r.POST.get('password')
        if u=='admin':
            if p=='1234':
                return redirect(index2)
            else:
                messages.info(r,"incorrect password",extra_tags='login')
                return redirect(login)
            
        elif User.objects.filter(username=u).exists():
            usr=User.objects.filter(username=u).first()
            user = authenticate(username=u, password=p)
            if user is not None:
                r.session['id']=[usr.id] 
                

                return redirect(index)
            else:
                messages.info(r,"incorrect password",extra_tags='login')
                return redirect(login)
        else:
            messages.info(r,"username not found",extra_tags='login')
            return redirect(login)
    return render(r,'login.html')
def signup(r):
    if r.method=='POST':
        n=r.POST.get('name')
        m=r.POST.get('mobile')
        e=r.POST.get('email')
        u=r.POST.get('username')
        p=r.POST.get('password')
        p2=r.POST.get('confirm')
        if p==p2:
            if User.objects.filter(username=u).exists():
                messages.info(r,'username already exist',extra_tags='signup')
                return redirect(signup)
            elif User.objects.filter(email=e).exists():
                messages.info(r,'email already exist',extra_tags='signup')
                return redirect(signup)
            else:
                vall=User.objects.create_user(first_name=n,last_name=m,email=e,username=u,password=p)
                vall.save()
                usr=User.objects.filter(username=u).first()
                r.session['id']=[usr.id] 
                return redirect(index)
        else:
            messages.info(r,"passwor not match",extra_tags='signup')
            return redirect(signup)
    return render(r,'login.html')
def logout(r):
    if 'id'in r.session:
        r.session.flush()
        return redirect(index)
    return redirect(r,'index.html')
def profile(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        usr=User.objects.filter(id=val).first()
        p=profilepic.objects.filter(user=usr).first()
        cnt=c.count()
        wcnt=w.count()
        return render(r,'profile.html',{'usr':usr,'cnt':cnt,'wcnt':wcnt,'p':p})
    return redirect(login)
def editprofile(r):
    se=r.session.get('id')
    val=se[0]
    w=wish.objects.filter(usr=val).all()
    c=mycart.objects.filter(usr=val).all()
    usr=User.objects.filter(id=val).first()
    p=profilepic.objects.filter(user=usr).first()
    print(p)
    cnt=c.count()
    wcnt=w.count()
    return render(r,'editprofile.html',{'usr':usr,'cnt':cnt,'wcnt':wcnt,'p':p})    
def editprofile2(r):
    se=r.session.get('id')
    val=se[0]
    w=wish.objects.filter(usr=val).all()
    c=mycart.objects.filter(usr=val).all()
    # l=User.objects.get(id=val)
    b=User.objects.get(id=val)
    p=profilepic.objects.filter(user=b).first()
    cnt=c.count()
    wcnt=w.count()
    if r.method=='POST':
        b.first_name=r.POST.get('name')
        b.email=r.POST.get('email')
        b.last_name=r.POST.get('mobile')
        pic=r.FILES.get('img')
        if pic==None:
            b.save()
        else:
            if p:
                p.user=b
                p.propic=pic
                b.save()
                p.save()
            else:
                cr=profilepic.objects.create(user=b,propic=pic)
                cr.save()
        return redirect(profile)
    return render(r,'profile.html',{'b':b,'cnt':cnt,'wcnt':wcnt})
def preset(r):
    se=r.session.get('id')
    val=se[0]
    w=wish.objects.filter(usr=val).all()
    c=mycart.objects.filter(usr=val).all()
    usr=User.objects.filter(id=val).first()
    p=profilepic.objects.filter(user=usr).first()
    cnt=c.count()
    wcnt=w.count()
    return render(r,'preset.html',{'usr':usr,'cnt':cnt,'wcnt':wcnt,'p':p})
def preset2(r):
    se=r.session.get('id')
    val=se[0]
    w=wish.objects.filter(usr=val).all()
    c=mycart.objects.filter(usr=val).all()
    usr=User.objects.filter(id=val).first()
    p=profilepic.objects.filter(user=usr).first()
    cnt=c.count()
    wcnt=w.count()
    if r.method=='POST':
        np=r.POST.get('password')
        cnp=r.POST.get('cnewpassword')
        user = authenticate(username=usr.username, password=r.POST.get('oldpassword'))
        if user is not None:
            if np==cnp:
                user.set_password(np)
                user.save()
                print('change')
                return redirect(profile)
            else:
                messages.info(r,"passwor dosen't exist",extra_tags='preset')
                return redirect(preset)
        else:
            messages.info(r,"password wrong",extra_tags='preset')
            return redirect(preset)
    return render(r,'profile.html',{'usr':usr,'cnt':cnt,'wcnt':wcnt,'p':p})
def deleteprofile(r):
    se=r.session.get('id')
    val=se[0]
    l=User.objects.filter(id=val).first()
    l.delete()
    r.session.flush()
    return redirect(login)
def tr(r):
    return render(r,'tr.html')
def checkout(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        usr=User.objects.filter(id=val).first()
        p=profilepic.objects.filter(user=usr).first()
        cnt=c.count()
        wcnt=w.count()
        cl={}
        t=0
        for i in c:
            # p=productdet.objects.filter(id=i.products).first()
            cl[i.products]=[i.quantity,i.id,i.products.discount*i.quantity]
            t=t+(i.products.discount*i.quantity)
        
        return render(r,'checkout.html',{'usr':usr,'cl':cl,'cnt':cnt,'wcnt':wcnt,'t':t,'p':p})
    return redirect(login)
def thanku(r):
    if 'id' in r.session:
        se=r.session.get('id')
        val=se[0]
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        usr=User.objects.filter(id=val).first()
        cnt=c.count()
        wcnt=w.count()
        return render(r,'thanku.html',{'usr':usr,'cnt':cnt,'wcnt':wcnt})

    return render(r,'thanku.html')
def placeorder(r):
    if 'id' in r.session:
        se = r.session.get('id')
        val = se[0]
        usr = User.objects.get(id = val)
        c = mycart.objects.filter(usr=val).all()
        t=0
        for i in c:
            t=t+(i.products.discount*i.quantity)
        if r.method == 'POST':
            if profilee.objects.filter(user=usr) == None:
                userprofile = profile()
                userprofile.user = usr
                userprofile.fname = r.POST.get('fname')
                userprofile.lname = r.POST.get('lname')
                userprofile.email = r.POST.get('email')
                userprofile.phone = r.POST.get('phone')
                userprofile.address = r.POST.get('address')
                userprofile.city = r.POST.get('city')
                userprofile.state = r.POST.get('state')
                userprofile.country = r.POST.get('country')
                userprofile.pincode = r.POST.get('pincode')
                userprofile.save()

            neworder = order()
            neworder.user = usr
            neworder.fname = r.POST.get('fname')
            neworder.lname = r.POST.get('lname')
            neworder.email = r.POST.get('email')
            neworder.phone = r.POST.get('phone')
            neworder.address = r.POST.get('address')
            neworder.city = r.POST.get('city')
            neworder.state = r.POST.get('state')
            neworder.country = r.POST.get('country')
            neworder.pincode = r.POST.get('pincode')

            neworder.total_price = t

            neworder.payment_mode = r.POST.get('payment_mode')
            neworder.payment_id = r.POST.get('payment_id')

            trackno = 'sglass'+str(random.randint(1111111,9999999))
            while order.objects.filter(tracking_no=trackno) is None:
                trackno = 'sglass'+str(random.randint(1111111,9999999))
            neworder.tracking_no = trackno
            neworder.save()

            for item in c:
                orderitem.objects.create(
                    orderdet = neworder,
                    product = item.products,
                    price = item.products.discount,
                    quantity = item.quantity
                )

            mycart.objects.filter(usr=val).delete()

            messages.success(r, 'Your order has been placed successfully')

            payMode = r.POST.get('payment_mode')
            if payMode == "Razorpay":
                return JsonResponse({'status':'Your order has been placed successfully'})

        return redirect(index)
def razorpaycheck(r):
    if 'id' in r.session:
        se = r.session.get('id')
        val = se[0]
        c = mycart.objects.filter(usr=val).all()
        t=0
        for i in c:
            t=t+(i.products.discount*i.quantity)

    return JsonResponse({
        'total_price':t
    })
def orderss(r):
    if 'id' in r.session:
        se = r.session.get('id')
        val = se[0]
        usr = User.objects.get(id=val)
        w=wish.objects.filter(usr=val).all()
        c=mycart.objects.filter(usr=val).all()
        p=profilepic.objects.filter(user=usr).first()
        cnt=c.count()
        wcnt=w.count()
        o = order.objects.all()
        l=[]
        for i in o:
            if i.user==usr:
                l.append(i)
        return render(r,'myorders.html',{'l':l,'usr':usr,'cnt':cnt,'wcnt':wcnt,'p':p})
    return render(r,'myorders.html')

# admin



def base2(r):
    return render(r,'admin/base2.html')
def products(r):
    l=productdet.objects.all()
    return render(r,'admin/products.html',{'l':l})
def index2(r):
    obj=productdet.objects.all()
    coun = User.objects.all()
    prod = productdet.objects.all()
    produ = len(prod)
    count = len(coun)-1
    l=[]
    for i in obj:
        if len(l)<3:
            l.append(i)
        else:
            pass
        return render(r,'admin/index2.html',{'l':l,'count':count,'produ':produ})
def addproducts(r):
    if r.method=='POST':
        n=r.POST.get('name')
        p=r.POST.get('price')
        dc=r.POST.get('discription')
        m=r.POST.get('model')
        cl=r.POST.get('color')
        d=r.POST.get('discount')
        q=r.POST.get('quantity')
        c=r.POST.get('category')
        i=r.FILES.get('image')
        l=productdet.objects.create(name=n,price=p,discription=dc,model=m,color=cl,discount=d,quantity=q,category=c,image=i,)
        l.save()
        return redirect(products)
    return render(r,'admin/addproduct.html') 
def editproducts(r,wal):
    l=productdet.objects.filter(id=wal).first()
    return render(r,'admin/editproduct.html',{'l':l})
def sorder(r,wal):
    usr = User.objects.get(id=wal)
    o = order.objects.all()
    l=[]
    n=[]
    if usr.first_name not in n:
         n.append(usr.first_name)
    for i in o:
        if i.user==usr:
            l.append(i)
    return render(r,'admin/sorder.html',{'l':l,'n':n}) 
def editproducts2(r,wal):
    l=productdet.objects.get(id=wal)
    if r.method=='POST':
        l.name=r.POST.get('name')
        l.price=r.POST.get('price')
        l.discription=r.POST.get('discription')
        l.model=r.POST.get('model')
        l.color=r.POST.get('color')
        l.discount=r.POST.get('discount')
        l.quantity=r.POST.get('quantity')
        l.category=r.POST.get('category')
        img=r.FILES.get('image')
        if img==None:
            l.save()
        else:
            l.image=r.FILES.get('image')
            l.save()
        return redirect(products)
    return render(r,'admin/editproduct.html',{'l':l}) 
def delpro(r,wal):
    l=productdet.objects.filter(id=wal).first()
    l.delete()
    return redirect(products)
def users(r):
    o = order.objects.all()
    p=[]
    for i in o:
        p.append(i.user.id)
    l=User.objects.all()
    return render(r,'admin/users.html',{'l':l,'p':p})
def mess1(r):
    l=msg.objects.all()
    return render(r,'admin/messeges.html',{'l':l})
def reply(r,em):
    l=msg.objects.filter(id=em).first()
    return render(r,"admin/replymail.html",{'l':l})
def replymail(r,em):
    if r.method=='POST':
        l=msg.objects.filter(id=em).first()
        n=r.POST.get('message')
        send_mail('Reply From Admin', f'{n}','settings.EMAIL_HOST_USER', [l.email],fail_silently=False)
        return redirect(mess1)
    return render(r, 'admin/replymail.html')
def orders(r):
    l=order.objects.all()
    return render(r,'admin/orders.html',{'l':l})
def statusup(r,wal):
    if r.method == "POST":
        st = order.objects.get(id=wal)
        st.status = r.POST.get('status')
        st.save()
        return redirect(orders)
def logout2(r):
    return redirect(index)
