from django import forms
from .models import Customer, ShippingAddress

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email']
        labels ={'name': "Customer Name and Email", 'email': ""}
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Type here the name" }),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Type here the email" })
        }

class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address','city','state','zipcode']
        labels = {'address': "Customer address and city", 'city': "", 'state': "Customer state and zipcode", 'zipcode': ""}


        widgets= {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Type here the Address" }),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Type here the city" }),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Type here the state"}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Type here the zipcode"})
        }