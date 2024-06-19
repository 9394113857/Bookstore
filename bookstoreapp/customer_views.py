from django.shortcuts import render,redirect
from bookstoreapp.models import Contact,Customer,Bookstore,Merchant,Addcart,Feedback
from bookstoreapp.forms import ContactForms,CustomerForms,BookstoreForms,AddcartForms,FeedbackForms
# Create your views here.
def index(request):
    book=Bookstore.objects.all()
    return render(request, "index.html", {"books":book})


def about(request):
    return render(request, "about.html", {})


def menu(request):
    book=Bookstore.objects.all()
    menu=Bookstore.objects.all()
    return render(request, "menu.html", {"books":book, "menus":menu})


def services(request):
    return render(request, "services.html", {})


def blog(request):
    return render(request, "blog.html", {})


def contact(request):
    return render(request, "contact.html", {})


def contactpage(request):
    if request.method == "POST":
        contact = ContactForms(request.POST)
        print('hi')
        if contact.is_valid():
            print(contact.errors)
            contact.save()
            return render(request, "contact.html", {"msg": "Contact Posted"})
    return render(request, "contact.html", {})


def customer(request):
    return render(request, "customer.html", {})


def customer_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        customer = Customer.objects.filter(email=email, password=password)
        if customer.exists():
            request.session['email'] = email
            return render(request, "customerprofile.html", {"msg": email})
        else:
            return render(request, "customer.html", {"msg": "Invalid Data"})
    return render(request, "customer.html", {})


def customer_regpage(request):
    return render(request,"customer_regpage.html",{})


def reg(request):
    if request.method == "POST":
        email = request.POST["email"]
        print("hai")
        if Customer.objects.filter(email=email).exists():
            print("email already taken")
            return render(request, "customer_regpage.html", {"msg": "This Email Already Exists"})
        else:
            form = CustomerForms(request.POST)
            print("error:", form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return render(request, "customer.html", {"msg": "Registraation Successful"})
                except Exception as e:
                    print(e)
                    print("hii")
            return render(request, "customer_regpage.html", {"msg": "Registration Not Success"})


def customer_logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request, "customer.html", {})


def customer_details_display(request):
    email = request.session['email']
    customers = Customer.objects.get(email=email)
    print('ram')
    return render(request, "customer_details.html", {"customer": customers})

def is_customer(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def customer_change_password(request):
    if is_customer(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                user = Customer.objects.get(email=email, password=password)
                user.password = newpassword
                user.save()
                msg = 'Password Updated Successfully'
                return render(request, "customer change password.html", {"msg": msg})
            except:
                msg = 'Invalid Data'
                return render(request, "customer change password.html", {"msg": msg})
        return render(request, "customer change password.html", {})
    else:
        return render(request, "customer change password.html", {})


def customer_delete(request, email):
    user = Customer.objects.get(email=email)
    user.delete()
    return redirect("/customer_regpage")


def customer_edit(request, email):
    customer = Customer.objects.get(email=email)
    return render(request, "customer_edit.html", {"customer": customer})


def customer_update(request):
    if request.method == "POST":
        print("error:")
        email = request.POST["email"]
        print("hello")
        customer = Customer.objects.get(email=email)
        customer = CustomerForms(request.POST, instance=customer)
        print("error:", customer.errors)
        if customer.is_valid():
            print("error:", customer.errors)
            customer.save()
        return redirect("/customer_details_display")
    return redirect("/customer_details_display")

def customer_view_book(request):
    store= Merchant.objects.all()
    return render(request,"customer_view_book.html",{"stores":store})


def view_menu(request,id):
    merchant = Merchant.objects.get(id=id)
    book = Bookstore.objects.filter(merchant_id=merchant.id)
    print("hii")
    return render(request, "view_menu.html", {"books": book,"store":merchant.store,"id":merchant.id})


def customer_order_book(request,id):
    email= request.session['email']
    print(email)
    customer =  Customer.objects.get(email=email)
    book = Bookstore.objects.get(id=id)
    if request.method=="POST":
        books=AddcartForms(request.POST)
        print("errors",books.errors)
        print('hii')
        if books.is_valid():
            print("error:",books.errors)
            books.save()
            return render(request,"add_to_cart.html",{"msg":"Success","customer":customer.id,"book":book})
    return render(request,"add_to_cart.html",{"customer":customer.id,"book":book})


def customer_view_order(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    print("hi11")
    details = Addcart.objects.filter(customer_id=customer.id)
    print("ryy")
    return render(request, "customer_view_order.html", {"orders": details})


def feedback(request,id):
    email=request.session['email']
    customer=Customer.objects.get(email=email)
    merchant=Merchant.objects.get(id=id)
    if request.method=="POST":
        feedback=FeedbackForms(request.POST)
        if feedback.is_valid():
            feedback.save()
            return render(request,"feedback.html",{"msg":"Success","customer":customer.id,"merchant":merchant.id})
    return render(request, "feedback.html", {"msg":"Not Posted","customer": customer.id, "merchant": merchant.id})


def customer_view_feedback(request,id):
    merchant=Merchant.objects.get(id=id)
    feedback=Feedback.objects.filter(merchant_id=merchant.id)
    return render(request,"customer_view_feedback.html",{"feedbacks":feedback,"merchant":merchant.store})


def customerprofile(request):
    return render(request,"customerprofile.html",{})

def cancel(request,id):
    cancel=Addcart.objects.get(id=id)
    cancel.status=5
    cancel.save()
    return redirect("/customer_view_order")