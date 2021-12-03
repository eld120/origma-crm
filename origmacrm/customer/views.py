# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, TemplateView

# Create your views here.
from origmacrm.customer.models import Customer


class DashboardView(LoginRequiredMixin, TemplateView):
    """handles CRM home page with search functionality"""

    template_name = "customer/dashboard.html"


class CustomerListView(LoginRequiredMixin, ListView):
    """returns the results of a search of customer accounts"""

    model = Customer
    template_name = "dashboard.html"

    # could be useful to allow searches across different db fields
    def get_queryset(self):
        user_query = self.request.GET.get("q")
        # eventually implement prefetch_related to reduce db queries
        return Customer.objects.filter(
            Q(dba__icontains=user_query) & Q(dba__startswith=user_query)
        )


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = ".html"
    success_url = "CustomerDetailView:slug"


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = ".html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customer"] = get_object_or_404(Customer, None)
        return context
