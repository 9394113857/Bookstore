from django.db import models

# Create your models here.

class Admin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100)

    class Meta:
        db_table="Admin"

class Contact(models.Model):
    name=models.CharField(max_length=100)
    contactemail=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    msg=models.TextField(max_length=500)

    class Meta:
        db_table="contact"

class Customer(models.Model):
    fullname=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    address=models.TextField(max_length=400)

    class Meta:
        db_table="Customer"


class Merchant(models.Model):
    fullname=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    store=models.CharField(max_length=100)
    img=models.ImageField()
    address=models.TextField(max_length=400)

    class Meta:
        db_table="merchant"


class Bookstore(models.Model):
    merchant=models.ForeignKey(Merchant,on_delete=models.CASCADE)
    bookname=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    image=models.ImageField()
    cost=models.BigIntegerField()
    year=models.BigIntegerField()
    discount=models.BigIntegerField()
    description=models.TextField(max_length=100)
    categoty=models.CharField(max_length=100)

    class Meta:
        db_table="book_details"


class Addcart(models.Model):
    book=models.ForeignKey(Bookstore,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    add=models.CharField(max_length=100)
    cart=models.CharField(max_length=100)
    cost=models.BigIntegerField()
    discount=models.BigIntegerField()
    finalcost=models.BigIntegerField()
    status=models.IntegerField(default=0)
    email=models.EmailField(max_length=100)
    class Meta:
        db_table="order_book"


class Feedback(models.Model):
    merchant=models.ForeignKey(Merchant,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    text=models.TextField(max_length=100)
    rating=models.IntegerField()

    class Meta:
        db_table="feedbacks"





