from datetime import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .validators import phone_validator

ACTIVE_OPTIONS = (("active", "Active"), ("archived", "Archived"))


class Customer(models.Model):
    """A model that describes a User/business, vendors, or customers"""

    CUSTOMER_ROLES = (
        ("customer", "Customer"),
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
    active = models.CharField(
        _("Account Status"), choices=ACTIVE_OPTIONS, max_length=25
    )
    start_date = models.DateField(_("Start Date"), auto_now_add=True)
    end_date = models.DateField(
        _("End Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    created_date = models.DateTimeField(_("Created Date"), auto_now_add=True)
    industry = models.CharField(_("Industry"), choices=INDUSTRY_OPTIONS, max_length=100)
    website = models.URLField(_("Webiste"), max_length=200)
    account_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_Account",
        verbose_name=_("Account Manager"),
        on_delete=models.PROTECT,
    )
    ein = models.CharField(_("EIN"), max_length=50)
    slug = models.SlugField(max_length=250)

    class Meta:
        verbose_name_plural = _("Customers")

    def __str__(self) -> str:
        return f"{self.name} dba {self.dba}"

    def archive_customer(self):
        if self.active == "archived":
            self.end_date == datetime.datetime.now()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.dba)

        super(Customer, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("customer:customer-detail", kwargs={"slug": self.slug})


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
    COUNTRIES = (("ca", "CA"), ("mx", "MX"), ("us", "US"))

    LOCATION_TYPE = (
        ("billing", "Billing Address"),
        ("billing/shipping", "Billing/Shipping"),
        ("shipping", "Shipping Address"),
    )

    active = models.CharField(
        _("Location Status"), choices=ACTIVE_OPTIONS, max_length=25
    )
    role = models.CharField(_("Address Type"), choices=LOCATION_TYPE, max_length=20)
    location = models.ForeignKey(
        "customer.Customer", verbose_name=_("Location"), on_delete=models.PROTECT
    )
    created_on = models.DateField(_("Created Date"), auto_now_add=True)
    last_modified = models.DateTimeField(
        _("Last Modified Date"), auto_now=False, auto_now_add=True
    )
    address_1 = models.CharField(_("Address 1"), max_length=50)
    address_2 = models.CharField(_("Address 2"), max_length=50, blank=True, null=True)
    # address_3 = models.CharField(_(""), max_length=50)
    city = models.CharField(_("City"), max_length=50)
    state = models.CharField(_("State"), choices=STATE_CODES, max_length=50)
    zip_code = models.CharField(_("Zip Code"), max_length=50)
    phone = models.CharField(_("Phone"), validators=[phone_validator], max_length=15)
    # fax = models.PhoneNumberField(_("")) - phonenumber field needs to be imported from Google's libphonenumber library
    country = models.CharField(_("Country"), choices=COUNTRIES, max_length=2)
    # tax_jurisdiction = models.CharField(_("Tax Jurisdiction"), max_length=50)
    # ^- This really needs to be a foreignkey to a tax jurisdiction table

    class Meta:
        verbose_name_plural = _("Addresses")

    def __str__(self) -> str:
        return f"{self.address_1} {self.address_2} in {self.city} {self.state}"

    def get_address(self):
        return f"{self.address_1} {self.address_2}\n{self.city} {self.state} {self.zip_code}\n{self.phone}"


class Contact(models.Model):
    """class designed to capture all client/customer employees"""

    CONTACT_ROLES = (
        ("owner", "Owner"),
        ("manager", "Manager"),
        ("sales", "Sales"),
        ("service", "Service"),
        ("accounting", "Accounting"),
        ("executive", "Executive"),
        ("product development", "Product Development"),
        ("marketing", "Marketing"),
        ("logistics", "Logistics"),
        ("purchasing", "Purchasing"),
        ("IT", "IT"),
        ("not employed", "Not Employed"),
    )
    name = models.CharField(_("Name"), max_length=50)
    employee_location = models.ForeignKey(
        "customer.Address",
        verbose_name=_("Employee Location"),
        on_delete=models.PROTECT,
    )
    position = models.CharField(
        _("Position or Role"), choices=CONTACT_ROLES, max_length=30
    )
    description = models.TextField(_("Contact Notes"))
    phone_1 = models.CharField(
        _("Phone 1"), validators=[phone_validator], max_length=15, null=True, blank=True
    )
    phone_2 = models.CharField(
        _("Phone 2"), validators=[phone_validator], max_length=15, null=True, blank=True
    )
    email_1 = models.EmailField(_("Email 1"), max_length=254, null=True, blank=True)
    email_2 = models.EmailField(_("Email 2"), max_length=254, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} is {self.position} at {self.employer} "
