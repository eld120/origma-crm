from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import phone_validator


class Customer(models.Model):
    """A model that describes a User/business, vendors, or customers"""

    CUSTOMER_ROLES = (
        ("customer", "Customer"),
        ("client", "Client"),
        ("vendor", "Vendor"),
        ("employee", "Employee"),
    )
    INDUSTRY_OPTIONS = (
        ("agriculture", "Agriculture"),
        ("arts entertainment", "Arts & Entertainment"),
        ("construction", "Construction"),
        ("education", "Education"),
        ("energy", "Energy"),
        ("food", "Food & Hospitality"),
        ("finance", "Finance and Insurance"),
        ("healthcare", "Healthcare"),
        ("manufacturing", "Manufacturing"),
        ("mining", "Mining"),
        ("other", "Other Services"),
        ("services", "Professional, Scientific, and Tech Services"),
        ("real estate", "Real Estate"),
        ("retail", "Retail"),
        ("transportation", "Transportation & Logistics"),
        ("utilities", "Utilities"),
        ("wholesale", "Wholesale"),
    )
    role = models.CharField(_("Role"), choices=CUSTOMER_ROLES, max_length=50)
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
    account_manager = models.ForeignKey(
        "customer.Customer",
        related_name="%(class)s_Account",
        verbose_name=_("Account Manager"),
        on_delete=models.PROTECT,
    )
    ein = models.CharField(_("EIN"), max_length=50)
    industry = models.CharField(_("Industry"), choices=INDUSTRY_OPTIONS, max_length=100)
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

    STATE_CODES = (
        ("AL", "Alabama"),
        ("AK", "Alaska"),
        ("AS", "American Samoa"),
        ("AZ", "Arizona"),
        ("AR", "Arkansas"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DE", "Delaware"),
        ("DC", "District of Columbia"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("GU", "Guam"),
        ("HI", "Hawaii"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("IA", "Iowa"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiana"),
        ("ME", "Maine"),
        ("MD", "Maryland"),
        ("MA", "Massachusetts"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MS", "Mississippi"),
        ("MO", "Missouri"),
        ("MT", "Montana"),
        ("NE", "Nebraska"),
        ("NV", "Nevada"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NY", "New York"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("MP", "Northern Mariana Islands"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvania"),
        ("PR", "Puerto Rico"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VT", "Vermont"),
        ("VI", "Virgin Islands"),
        ("VA", "Virginia"),
        ("WA", "Washington"),
        ("WV", "West Virginia"),
        ("WI", "Wisconsin"),
        ("WY", "Wyoming"),
    )

    ACTIVE_FLAG = (("active", "Active"), ("archived", "Archived"))

    active = models.CharField(_("Activate Account"), choices=ACTIVE_FLAG, max_length=50)
    created_on = models.DateField(_("Created Date"), auto_now=False, auto_now_add=False)
    last_modified = models.DateTimeField(
        _("Last Modified Date"), auto_now=False, auto_now_add=True
    )
    address_1 = models.CharField(_("Address 1"), max_length=50)
    address_2 = models.CharField(_("Address 2"), max_length=50)
    # address_3 = models.CharField(_(""), max_length=50)
    city = models.CharField(_("City"), max_length=50)
    state = models.CharField(_("State"), choices=STATE_CODES, max_length=50)
    zip_code = models.CharField(_("Zip Code"), max_length=50)
    phone = models.CharField(_("Phone"), validators=[phone_validator], max_length=15)
    # fax = models.PhoneNumberField(_("")) - phonenumber field needs to be imported from Google's libphonenumber library
    country = models.CharField(_("Country"), max_length=2)
    # tax_jurisdiction = models.CharField(_("Tax Jurisdiction"), max_length=50)
    # ^- This really needs to be a foreignkey to a tax jurisdiction table

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
    phone_1 = models.CharField(
        _("Phone 1"), validators=[phone_validator], max_length=15
    )
    phone_2 = models.CharField(
        _("Phone 2"), validators=[phone_validator], max_length=15
    )
    # phone_3 = models.PhoneNumberField(_(""))
    # phone_4 = models.PhoneNumberField(_(""))
    email_1 = models.EmailField(_(""), max_length=254)
    email_2 = models.EmailField(_(""), max_length=254)
