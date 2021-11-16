from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class BaseInteraction(models.Model):
    """class designed to capture all communication between the business and client"""

    class Meta:
        abstract = True

    employee = models.ForeignKey(
        "users.User", verbose_name=_("Employee"), on_delete=models.CASCADE
    )
    date = models.DateField(_("Date"), auto_now=True, auto_now_add=False)
    contact = models.ForeignKey(
        "customer.Contact",
        related_name="%(class)s_direct_contact",
        verbose_name=_("Contact"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    business = models.ForeignKey(
        "customer.Customer",
        related_name="%(class)s_business_client",
        verbose_name=_("Business"),
        on_delete=models.CASCADE,
    )
    notes = models.TextField(_(""))
    initiative = models.ForeignKey(
        "interaction.Initiative", verbose_name=_("Initiative"), on_delete=models.CASCADE
    )
    involved_contacts = models.ForeignKey(
        "customer.Customer",
        related_name="%(class)s_additional_contacts",
        verbose_name=_(""),
        on_delete=models.CASCADE,
    )
    expected_sales = models.DecimalField(
        _("Expected Sales"), max_digits=9, decimal_places=2, default=0.00
    )
    realized_sales = models.DecimalField(
        _("Realized Sales"), max_digits=9, decimal_places=2, default=0.00
    )

    def assign_user(self, employee):
        self.employee = employee


class Task(BaseInteraction):
    """interaction class to capture actionable activities"""

    def notification(self, users):
        # todo
        # tasks should do things when they are created, when state changes, and when they are completed
        pass


class Interaction(BaseInteraction):
    """interaction class to capture non-actionable activities"""

    def clone_task(self):
        # should we allow users to clone an activity into a task for future follow up?
        pass


class Initiative(models.Model):
    """Captures business initiatives and allows users to create/use/track/report on their performance"""

    CAMPAIGN_CHOICES = (
        ("bundle", "Bundle"),
        ("overstock", "Overstock"),
        ("closeout", "Closeout"),
        ("special price", "Special Price"),
    )

    PROGRESS_CHOICES = (
        ("open", "Open"),
        ("closed", "Closed"),
        ("negotiating", "Negotiating"),
        ("won", "Won"),
        ("lost", "Lost"),
    )

    ORIGIN_CHOICES = (
        ("promotion", "Promotion"),
        ("email", "Email"),
        ("outbound call", "Outbound Call"),
        ("referral", "Referral"),
        ("inbound call", "Inbound Call"),
        ("event", "Event"),
    )

    campaign = models.CharField(_("Campaign"), choices=CAMPAIGN_CHOICES, max_length=50)
    start_date = models.DateField(_("Start Date"), auto_now=False, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    description = models.TextField(_("Description"))
    status = models.CharField(_("Status"), choices=PROGRESS_CHOICES, max_length=50)
    origin = models.CharField(_("Origin"), choices=ORIGIN_CHOICES, max_length=50)
    expected_sales = models.DecimalField(
        _("Expected Sales"), max_digits=9, decimal_places=2, default=0.00
    )
    realized_sales = models.DecimalField(
        _("Realized Sales"), max_digits=9, decimal_places=2, default=0.00
    )

    # @property
    # def initiative_status(self):
    #     return self._status
