"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urlbook
"""
from django.contrib import admin
from django.urls import path
from bookstoreapp import customer_views as s
from bookstoreapp import merchant_views as m
from bookstoreapp import admin_views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #Customer Urls

    path('admin/', admin.site.urls),
    path('',s.index,name="index"),
    path('about/',s.about,name="about"),
    path('menu/',s.menu,name="menu"),
    path('services/',s.services,name="services"),
    path('blog/',s.blog,name="blog"),
    path('contact/',s.contact,name="contact"),
    path('contactpage/',s.contactpage,name="contactpage"),
    path('customer/',s.customer,name="customer"),
    path('customer_regpage/',s.customer_regpage,name="customer_regpage"),
    path('customer_login/',s.customer_login,name="customer_login"),
    path('customer_logout/',s.customer_logout,name="customer_logout"),
    path('reg/',s.reg,name="reg"),
    path('customer_details_display/',s.customer_details_display,name="customer_details_display"),
    path('customer_change_password/',s.customer_change_password,name="customer_change_password"),
    path('customer_delete/<str:email>',s.customer_delete,name="customer_delete"),
    path('customer_edit/<str:email>',s.customer_edit,name="customer_edit"),
    path('customer_update/',s.customer_update,name="customer_update"),
    path('customer_view_book/',s.customer_view_book,name="customer_view_book"),
    path('customer_view_order/',s.customer_view_order,name="customer_view_order"),
    path('view_menu/<int:id>',s.view_menu,name="view_menu"),
    path('customer_order_book/<int:id>',s.customer_order_book,name="customer_order_book"),
    path('feedback/<int:id>',s.feedback,name="feedback"),
    path('customerprofile/', s.customerprofile, name="customerprofile"),
    path('customer_view_feedback/<int:id>',s.customer_view_feedback,name="customer_view_feedback"),
    path('cancel/<int:id>',s.cancel,name="cancel"),

    #merchant urls

    path('merchant/', m.merchant, name="merchant"),
    path('merchant_login/', m.merchant_login, name="merchant_login"),
    path('merchant_regpage/', m.merchant_regpage, name="merchant_regpage"),
    path('merchant_register/', m.merchant_register, name="merchant_register"),
    path('merchant_logout/', m.merchant_logout, name="merchant_logout"),
    path('merchant_details_display/', m.merchant_details_display, name="merchant_details_display"),
    path('merchant_change_password/', m.merchant_change_password, name="merchant_change_password"),
    path('merchant_edit/<str:email>', m.merchant_edit, name="merchant_edit"),
    path('merchant_delete/<str:email>', m.merchant_delete, name="merchant_delete"),
    path('merchant_update/', m.merchant_update, name="merchant_update"),
    path('add_book_court/<int:id>', m.add_book_court, name="add_book_court"),
    path('merchant_view_book/<int:id>', m.merchant_view_book, name="merchant_view_book"),
    path('book_edit/<int:id>', m.book_edit, name="book_edit"),
    path('book_update/', m.book_update, name="book_update"),
    path('book_delete/<int:id>', m.book_delete, name="book_delete"),
    path('book_order/', m.book_order, name="book_order"),
    path('approve_slot/<int:id>', m.approve_slot, name="approve_slot"),
    path('reject_slot/<int:id>', m.reject_slot, name="reject_slot"),
    path('delivered_slot/<int:id>', m.delivered_slot, name="delivered_slot"),
    path('delivery/<int:id>',m.delivery,name="delivery"),
    path('merchant_view_feedback/', m.merchant_view_feedback, name="merchant_view_feedback"),
    path('feedback_delete/<int:id>', m.feedback_delete, name="feedback_delete"),
    path('merchantprofile/', m.merchantprofile, name="merchantprofile"),

    #Admin Urls

    path('admin_home/',views.admin_home,name="admin_home"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_change_pwd/',views.admin_change_pwd,name="admin_change_pwd"),
    path('view_contact/',views.view_contact,name="view_contact"),
    path('view_customer/',views.view_customer,name="view_customer"),
    path('view_merchant/',views.view_merchant,name="view_merchant"),
    path('view_order/',views.view_order,name="view_order"),

]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)