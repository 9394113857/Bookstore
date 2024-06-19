from django.contrib import admin

# Register your models here.
from bookstoreapp.models import Merchant
from bookstoreapp.models import Customer
from bookstoreapp.models import Contact
from bookstoreapp.models import Bookstore
from bookstoreapp.models import Addcart
from bookstoreapp.models import Feedback


admin.site.register(Merchant)
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Bookstore)
admin.site.register(Addcart)
admin.site.register(Feedback)
