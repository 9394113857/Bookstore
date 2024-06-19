from django import forms
from bookstoreapp.models import Contact,Customer,Merchant,Bookstore,Addcart,Feedback

class ContactForms(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"


class CustomerForms(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"



class MerchantForms(forms.ModelForm):
    class Meta:
        model=Merchant
        fields="__all__"


class BookstoreForms(forms.ModelForm):
    class Meta:
        model=Bookstore
        fields="__all__"


class AddcartForms(forms.ModelForm):
    class Meta:
        model=Addcart
        fields=('customer','add','cart','cost','discount','finalcost','book','email')


class FeedbackForms(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"