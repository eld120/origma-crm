from rest_framework import serializers

from origmacrm.customer import models


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
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


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
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


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
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
