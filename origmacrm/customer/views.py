# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic

from origmacrm.customer.forms import CustomerForm
from origmacrm.customer.models import Customer


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
    form_class = CustomerForm
    template_name = "customer/customer-create.html"

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
    form_class = CustomerForm
    template_name = "customer/customer-create.html"
