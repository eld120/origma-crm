from django import forms

from origmacrm.customer.models import Address, Contact, Customer


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "active",
            "role",
            "location",
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
            "active",
            "role",
            "end_date",
            "account_manager",
            "ein",
            "industry",
            "website",
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "name",
            "employee_location",
            "position",
            "description",
            "phone_1",
            "phone_2",
            "email_1",
            "email_2",
        )
