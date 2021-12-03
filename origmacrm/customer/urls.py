from django.urls import path

from .views import CustomerCreateView, CustomerDetailView, DashboardView

app_name = "customer"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("<slug:slug>/", CustomerDetailView.as_view(), name="customer-detail"),
    path("create-account/", CustomerCreateView.as_view(), name="customer-create"),
]
