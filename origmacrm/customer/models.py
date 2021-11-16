from django.db import models
from django.utils.translation import gettext_lazy as _


class CustRole(models.Model):
    class Meta:
        abstract = True

    CUSTOMER_ROLES = (
        ("customer", "Customer"),
        ("client", "Client"),
        ("vendor", "Vendor"),
        ("employee", "Employee"),
    )


# Create your models here.
class Customer(CustRole):
    """A model that describes a User/business, vendors, or customers"""

    role = models.CharField(_("Role"), max_length=50)
    dba = models.CharField(_("dba"), max_length=50)
    name = models.CharField(_("Legal Business Entity"), max_length=50)
    billing_address = models.ForeignKey(
        "customer.Address",
        related_name="%(class)s_billing_address",
        verbose_name=_("Billing Address"),
        on_delete=models.PROTECT,
    )
    shipping_address = models.ForeignKey(
        "customer.Address",
        related_name="%(class)s_shipping_address",
        verbose_name=_("Shipping Address"),
        on_delete=models.PROTECT,
    )
    start_date = models.DateField(_("Start Date"), auto_now=False, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    active = models.CharField(_("Active"), max_length=50)
    archive = models.CharField(_("Archive"), max_length=50)
    created_date = models.DateTimeField(
        _("Created Date"), auto_now=False, auto_now_add=False
    )
    created_by = models.ForeignKey(
        "customer.Customer",
        related_name="created_by_%(class)s",
        verbose_name=_("Created by"),
        on_delete=models.PROTECT,
    )
    ein = models.CharField(_("EIN"), max_length=50)
    industry = models.CharField(_("Industry"), max_length=50)
    website = models.URLField(_("Webiste"), max_length=200)
    contact = models.ForeignKey(
        "customer.Contact", verbose_name=_("Contact"), on_delete=models.PROTECT
    )

    class Meta:
        verbose_name_plural = _("Customers")

    def __str__(self):
        return f"{self.name} dba {self.dba}"


class Address(models.Model):
    """model to capture address data for all customer and contacts instances"""

    active = models.CharField(_(""), max_length=50)
    archived = models.CharField(_(""), max_length=50)
    created_on = models.DateField(_(""), auto_now=False, auto_now_add=False)
    last_modified = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)
    address_1 = models.CharField(_(""), max_length=50)
    address_2 = models.CharField(_(""), max_length=50)
    # address_3 = models.CharField(_(""), max_length=50)
    city = models.CharField(_(""), max_length=50)
    state = models.CharField(_(""), max_length=50)
    zip_code = models.CharField(_(""), max_length=50)
    # phone = Custom phone number validation can be provided through django.core.validators via RegexValidator
    # fax = models.PhoneNumberField(_("")) - phonenumber field needs to be imported from Google's libphonenumber library
    country = models.CharField(_(""), max_length=50)
    tax_jurisdiction = models.CharField(_(""), max_length=50)

    class Meta:
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return f"{self.address_1} {self.address_2} in {self.city} {self.state}"

    def get_absolute_url(self):
        pass

    @property
    def get_address(self):
        return f"{self.address_1} {self.address_2}\n{self.city} {self.state} {self.zip_code}\n{self.phone}"


class Contact(models.Model):
    """class designed to capture all client/customer employees"""

    name = models.CharField(_("Name"), max_length=50)
    position = models.CharField(_("Position or Role"), max_length=50)
    description = models.TextField(_("Contact Notes"))
    address = models.ForeignKey(
        "customer.Address", verbose_name=_(""), on_delete=models.CASCADE
    )
    # phone_1 = models.PhoneNumberField(_(""))
    # phone_2 = models.PhoneNumberField(_(""))
    # phone_3 = models.PhoneNumberField(_(""))
    # phone_4 = models.PhoneNumberField(_(""))
    email_1 = models.EmailField(_(""), max_length=254)
    email_2 = models.EmailField(_(""), max_length=254)
