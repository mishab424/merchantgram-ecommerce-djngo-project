from django import forms
from .models import Merchants,Product,Costomer,Order,Status,Help


class MerchantReg(forms.ModelForm):
    class Meta:
        model=Merchants
        fields='__all__'

class Product_items (forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class Costomer_Reg(forms.ModelForm):
    class Meta:
        model=Costomer
        fields='__all__'

class Order_details(forms.ModelForm):

    class Meta:
        model=Order
        fields='__all__'

class Help_form(forms.ModelForm):
    class Meta:
        model=Help
        fields='__all__'