from django import forms
from .models import Register,ProductDetail
#create your class form here

class RegisterForm(forms.ModelForm):
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={"placeholder":"Your name"}))
    phoneNo=forms.CharField(label='Phone Number',widget=forms.TextInput(attrs={"placeholder":"Your phoneno"}))
    email=forms.CharField(label='Email',widget=forms.TextInput(attrs={"placeholder":"Your email"}))
    password=forms.CharField(label='Password',widget=forms.TextInput(attrs={"placeholder":"Make sure it is strong!!"}))
    class Meta:
        model=Register
        fields='__all__'
        # same as below
        #  fields=['name','phoneNo','email','password']

class ProductDetailForm(forms.ModelForm):
    title=forms.CharField(label=' Product Title',widget=forms.TextInput(attrs={"placeholder":"Product name"}))
    price=forms.CharField(label='Price',widget=forms.TextInput(attrs={"placeholder":"Your price"}))
    summary=forms.CharField(label='Description',widget=forms.TextInput(attrs={"placeholder":"product description"}))
    sellerlocation=forms.CharField(label='Location',widget=forms.TextInput(attrs={"placeholder":"Your Location"}))
    quantity=forms.CharField(label='Product quantity',widget=forms.TextInput(attrs={"placeholder":"No of product"}))
    imagefile=forms.FileField(label='Upload Image')
    
    class Meta:
        model= ProductDetail
        fields= ['title','price','summary','sellerlocation','quantity','imagefile']