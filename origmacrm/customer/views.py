from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from origmacrm.customer import forms
from origmacrm.customer.models import Address, Customer


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    """handles CRM home page with search functionality"""

    template_name = "customer/dashboard.html"


class CustomerListView(LoginRequiredMixin, generic.ListView):
    """returns the results of a search of customer accounts"""

    model = Customer
    template_name = "customer/dashboard.html"
    context_object_name = "context"

    def get_queryset(self):
        user_query = self.request.GET.get("q")
        if user_query:
            return Customer.objects.filter(
                Q(dba__icontains=user_query) | Q(dba__startswith=user_query)
            )
        return Customer.objects.all()


class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.CustomerForm
    template_name = "customer/customer_create.html"
    context_object_name = "context"

    def get_success_url(self):
        return reverse_lazy(
            "customer:customer-detail", kwargs={"slug": self.kwargs["slug"]}
        )


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Customer
    template_name = "customer/customer.html"
    context_object_name = "context"


class CustomerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Customer
    form_class = forms.CustomerForm
    template_name = "customer/customer_update.html"


class AddressCreateView(LoginRequiredMixin, generic.CreateView):
    model: Address
    form_class = forms.AddressForm
    template_name = "customer/address_create.html"


@login_required
def customer_create(request):
    """template for customer and address creation/updates"""

    return render(request, "customer/customer_create.html")


def test_customer_create(request):
    customer_form = forms.CustomerForm(
        request.POST or None,
        initial={
            "account_manager": request.user,
            "active": "active",
            "role": "customer",
        },
    )

    if request.method == "POST":

        if "customer_data" in request.POST and customer_form.is_valid():

            customer = customer_form.save()
            return redirect("customer:test-customer-update", slug=customer.slug)

    return render(
        request,
        "customer/partials/edit_customer.html",
        {
            "customer_form": customer_form,
        },
    )


def test_customer_update(request, slug):
    customer = Customer.objects.get(slug=slug)
    customer_form = forms.CustomerForm(request.POST or None, instance=customer)

    if request.method == "POST" and customer_form.is_valid():
        customer = customer_form.save()
        return redirect("customer:test-customer-update", slug=customer.slug)

    return render(
        request,
        "customer/partials/edit_customer.html",
        {
            "customer_form": customer_form,
            "customer": customer,
        },
    )


def test_address_create(request):

    address_form = forms.AddressForm(
        request.POST or None,
        initial={"country": "us", "active": "active", "role": "billing"},
    )

    if request.method == "POST" and address_form.is_valid():
        address_form.save()

        return render(
            request,
            "customer/partials/edit_address.html",
            {
                "addres_form": address_form,
            },
        )

    return render(
        request,
        "customer/partials/edit_address.html",
        {
            "address_form": address_form,
        },
    )


def test_address_update(request, **kwargs):

    address = Address.objects.get(id=kwargs["id"])
    address_form = forms.AddressForm(request.POST or None, instance=address or None)

    if request.method == "POST" and address_form.is_valid():
        address = address_form.save()
        return redirect("customer:test-address-update", id=address.id)

    return render(
        request,
        "customer/partials/edit_address.html",
        {
            "address_form": address_form,
        },
    )
