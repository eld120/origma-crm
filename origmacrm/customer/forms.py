from django import forms

from .models import Address, Contact, Customer


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "active",
            "created_on",
            "last_modified",
            "address_1",
            "address_2",
            "city",
            "state",
            "zip_code",
            "phone",
            "country",
        )


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "dba",
            "name",
            "role",
            "billing_address",
            "shipping_address",
            "end_date",
            "active",
            "archive",
            "account_manager",
            "ein",
            "industry",
            "website",
            "contact",
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "name",
            "position",
            "description",
            "address",
            "phone_1",
            "phone_2",
            "email_1",
            "email_2",
        )
