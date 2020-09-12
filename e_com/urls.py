#url for app e_com 
from django.contrib import admin
from django.urls import path,re_path    #imported for the regular expression
from . import views                     #imported the views.py files here for our pipeline
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$',views.homepage,name="Homepage"),
    re_path(r'index/',views.homepage,name="Homepage"),
    re_path(r'register/',views.register_user,name="Register Page"),
    re_path(r'product/',views.store,name="Product Page"),
    re_path(r'supplierproductdetail/',views.product_detail,name="Seller Product Detail"),
    re_path(r'userlogin/',views.login_validation,name="User Login"),
    re_path(r'userloginshop/',views.loginproductView.as_view(),name="Shop Login"),
    re_path(r'Productsearch/',views.search,name="Search"),
    re_path(r'product_login_search/',views.login_search,name="Search"),
    re_path(r'item_view/',views.item_view,name="Item page"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
 

] 
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)#to append the following to the urlpatterns list
urlpatterns += staticfiles_urlpatterns()