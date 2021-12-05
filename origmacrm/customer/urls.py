from django.urls import path

from origmacrm.customer.views import (
    CustomerCreateView,
    CustomerDetailView,
    CustomerListView,
    CustomerUpdateView,
    DashboardView,
)

app_name = "customer"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("search/", CustomerListView.as_view(), name="customer-list"),
    path("<slug:slug>/", CustomerDetailView.as_view(), name="customer-detail"),
    path("create-account/", CustomerCreateView.as_view(), name="customer-create"),
    path(
        "update-account/<slug:slug>",
        CustomerUpdateView.as_view(),
        name="customer-update",
    ),
]
