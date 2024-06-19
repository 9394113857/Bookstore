from django.shortcuts import render, redirect
from bookstoreapp.models import Merchant, Bookstore, Addcart, Customer, Feedback
from bookstoreapp.forms import MerchantForms, BookstoreForms, AddcartForms, CustomerForms, FeedbackForms


def merchant(request):
    return render(request, "merchant.html", {})


def merchant_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        merchant = Merchant.objects.filter(email=email, password=password)
        if merchant.exists():
            request.session['email'] = email
            return render(request, "merchantprofile.html", {"msg": email})
        else:
            return render(request, "merchant.html", {"msg": "Invalid Data"})
    return render(request, "merchant.html", {})


def merchant_regpage(request):
    return render(request, "merchant_regpage.html", {})


def merchant_register(request):
    if request.method == "POST":
        email = request.POST["email"]
        print("hai")
        if Merchant.objects.filter(email=email).exists():
            print("email already taken")
            return render(request, "merchant_regpage.html", {"msg": "This Email Already Exists"})
        else:
            form = MerchantForms(request.POST, request.FILES)
            print("error:", form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return render(request, "merchant.html", {"msg": "Registration Successful"})
                except Exception as e:
                    print(e)
                    print("hii")
            return render(request, "merchant_regpage.html", {"msg": "Registration Not Success"})


def merchant_logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request, "merchant.html", {})


def merchant_details_display(request):
    email = request.session['email']
    merchant = Merchant.objects.get(email=email)
    print('ram')
    return render(request, "merchant_details.html", {"merchant": merchant})


def is_merchant(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def merchant_change_password(request):
    if is_merchant(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                user = Merchant.objects.get(email=email, password=password)
                user.password = newpassword
                user.save()
                msg = 'Password Updated Successfully'
                return render(request, "merchant change password.html", {"msg": msg})
            except:
                msg = 'Invalid Data'
                return render(request, "merchant change password.html", {"msg": msg})
        return render(request, "merchant change password.html", {})
    else:
        return render(request, "merchantprofile.html", {})


def merchant_edit(request, email):
    merchant = Merchant.objects.get(email=email)
    return render(request, "merchant_edit.html", {"merchant": merchant})


def merchant_update(request):
    if request.method == "POST":
        print("error:")
        email = request.POST["email"]
        print("hello")
        users = Merchant.objects.get(email=email)
        users = MerchantForms(request.POST, request.FILES, instance=users)
        print("error:", users.errors)
        if users.is_valid():
            print("error:", users.errors)
            users.save()
        return redirect("/merchant_details_display")
    return redirect("/merchant_details_display")


def merchant_delete(request, email):
    merchant = Merchant.objects.get(email=email)
    merchant.delete()
    return redirect("/merchant_regpage")


def add_book_court(request, id):
    email = request.session['email']
    merchant = Merchant.objects.get(email=email)
    book = Bookstore.objects.filter(id=id)
    if request.method == "POST":
        book = BookstoreForms(request.POST, request.FILES)
        print('hi')
        print("errors", book.errors)
        if book.is_valid():
            print(book.errors)
            book.save()
            return render(request, "add_book.html",
                          {"msg": "Success", "id": merchant.id, "store": merchant.store, "book": book})
    return render(request, "add_book.html", {"id": merchant.id, "book": book})


def merchant_view_book(request, id):
    merchant = Merchant.objects.get(id=id)
    book = Bookstore.objects.filter(merchant_id=merchant.id)
    print("hii")
    return render(request, "merchant_view_book.html", {"books": book, "store": merchant.store, "id": merchant.id})


def book_edit(request, id):
    book = Bookstore.objects.get(id=id)
    return render(request, "book_edit.html", {"book": book})


def book_update(request):
    global id
    email = request.session['email']
    merchant = Merchant.objects.get(email=email)
    if request.method == "POST":
        id = request.POST["id"]
        book = Bookstore.objects.get(id=id)
        book = BookstoreForms(request.POST, request.FILES, instance=book)
        print('hi')
        print(book.errors)
        if book.is_valid():
            print(book.errors)
            book.save()
            books = Bookstore.objects.filter(merchant_id=merchant.id)
            return render(request, "merchant_view_book.html", {"books": books, "store": merchant.store})
    return render(request, "merchant_view_book.html", {"id": id})


def book_delete(request, id):
    book = Bookstore.objects.get(id=id)
    book.delete()
    return render(request, "merchant_view_book.html", {})


def book_order(request):
    email=request.session["email"]
    print(email)
    orders = Addcart.objects.filter(email=email)
    print("hii1")
    return render(request, "merchant_view_bookings.html", {"orders": orders})


def approve_slot(request,id):
    approve = Addcart.objects.get(id=id)
    approve.status = 1
    approve.save()
    return redirect("/book_order")


def reject_slot(request,id):
    reject = Addcart.objects.get(id=id)
    reject.status = 2
    reject.save()
    return redirect("/book_order")


def delivered_slot(request,id):
    delivery = Addcart.objects.get(id=id)
    delivery.status = 3
    delivery.save()
    return redirect("/book_order")

def delivery(request,id):
    deli=Addcart.objects.get(id=id)
    deli.status=4
    deli.save()
    return redirect("/book_order")


def merchant_view_feedback(request):
    email = request.session['email']
    merchant = Merchant.objects.get(email=email)
    feedback = Feedback.objects.filter(merchant_id=merchant.id)
    return render(request, "merchant_view_feedback.html", {"feedbacks": feedback, "merchant": merchant.store})



def feedback_delete(request, id):
    feedback = Feedback.objects.get(id=id)
    feedback.delete()
    return redirect("/merchant_view_feedback")


def merchantprofile(request):
    return render(request, "merchantprofile.html", {})
