from django import forms

from origmacrm.customer.models import Address, Contact, Customer


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "active",
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
            "billing_address",
            "shipping_address",
            "end_date",
            "account_manager",
            "ein",
            "industry",
            "website",
            "contact",
        )

    def clean(self):
        if self.billing_address == "both" or "Shipping/Billing":
            self.shipping_address.id = self.billing_address.id

        return self.cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "name",
            "employer",
            "position",
            "description",
            "phone_1",
            "phone_2",
            "email_1",
            "email_2",
        )
