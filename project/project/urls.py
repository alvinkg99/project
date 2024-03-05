"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('search_view',views.search_view, name='search_view'),
    path('base',views.base,name='base'),
    path('glass',views.glass,name='glass'),
    path('shop',views.shop,name='shop'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('prodet/<wal>',views.prodet,name='prodet'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('prodet/addwish/<wal>',views.addwish,name='addwish'),
    path('delwish/<de>',views.delwish,name='delwish'),
    path('cart',views.cart,name='cart'),
    path('prodet/addcart/<wal>',views.addcart,name='addcart'),
    path('minuscart/<de>',views.minuscart,name='minuscart'),
    path('pluscart/<de>',views.pluscart,name='pluscart'),
    path('delcart/<de>',views.delcart,name='delcart'),
    path('profile',views.profile,name='profile'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('editprofile2',views.editprofile2,name='editprofile2'),
    path('preset',views.preset,name='preset'),
    path('preset2',views.preset2,name='preset2'),
    path('deleteprofile',views.deleteprofile,name='deleteprofile'),
    # path('msg',views.msg,name='msg'),



    path('tr',views.tr,name='tr'),

    

    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('try',views.tr,name='try'),
    path('checkout',views.checkout,name='checkout'),
    path('thanku',views.thanku,name='thanku'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='fp.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='fps.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='fpr.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='fpc.html'),name='password_reset_complete'),


    # admin
    path('base2',views.base2,name='base2'),
    path('index2',views.index2,name='index2'),
    path('products',views.products,name='products'),
    path('addproducts',views.addproducts,name='addproducts'),
    path('editproducts/<wal>',views.editproducts,name='editproducts'),
    path('editproducts/editproduct2/<wal>',views.editproducts2,name='editproducts2'),
    path('editproducts/delpro/<wal>',views.delpro,name='delpro'),

    path('users',views.users,name='users'),
    path('messeges',views.mess1,name='messages'),

    path('place-order', views.placeorder, name='placeorder'),
    path('proceed-to-pay', views.razorpaycheck, name='proceed-to-pay'),
    path('myorder', views.orderss, name='myorder'),
    path('reply/<em>',views.reply,name='reply'),
    path('reply/replymail/<em>',views.replymail,name='replymail'),
    path('orders',views.orders,name='orders'),
    path('statusup/<wal>',views.statusup,name="statusup"),
    path('sorder/<wal>',views.sorder,name='sorder'),

    

    path('logout2',views.logout2,name='logout2'),

   

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
