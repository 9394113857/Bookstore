from django.shortcuts import render,redirect
from bookstoreapp.models import Contact,Customer,Bookstore,Merchant,Addcart,Feedback,Admin
from bookstoreapp.forms import ContactForms,CustomerForms,BookstoreForms,AddcartForms,FeedbackForms

def admin_home(request):
    return render(request,"admin_home.html",{})


def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        login = Admin.objects.filter(email=email, password=password)
        if login.exists():
            request.session['email'] = email
            return render(request, 'admin_home.html', {"msg": email})
        else:
            return render(request, "admin.html", {"msg": "Invalid Data"})
    return render(request, "admin.html", {})


def is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def admin_change_pwd(request):
    if is_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                user = Admin.objects.get(email=email, password=password)
                user.password = newpassword
                user.save()
                msg = 'Password Updated Sucessfully'
                return render(request, "admin_change_pwd.html", {"msg": msg})
            except:
                msg = 'Invalid Data'
                return render(request, "admin_change_pwd.html", {"msg": msg})
        return render(request, "admin_change_pwd.html", {})
    else:
        return render(request, "admin_home.html", {})

def view_contact(request):
    contacts=Contact.objects.all()
    return render(request,"view_contact.html",{"contact":contacts})

def view_customer(request):
    customers=Customer.objects.all()
    return render(request,"view_customer.html",{"customer":customers})

def view_merchant(request):
    merchants=Merchant.objects.all()
    return render(request,"view_merchant.html",{"merchant":merchants})


def view_order(request):
    orders=Addcart.objects.all()
    return render(request,"view_order.html",{"order":orders})