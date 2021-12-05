# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from origmacrm.customer.forms import CustomerForm
from origmacrm.customer.models import Customer


class DashboardView(LoginRequiredMixin, TemplateView):
    """handles CRM home page with search functionality"""

    template_name = "customer/dashboard.html"


class CustomerListView(LoginRequiredMixin, ListView):
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


class CustomerCreateView(LoginRequiredMixin, CreateView):
    form_class = CustomerForm
    template_name = "customer-create.html"
    success_url = reverse_lazy("customer:CustomerDetailView")


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "customer/customer.html"
    context_object_name = "context"


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CustomerForm
    template_name = "customer-create.html"

    def get_queryset(self):
        slug = self.object.slug
        return Customer.objects.filter(customer_slug=slug)
