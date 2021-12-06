from django.urls import path

from origmacrm.customer import views

app_name = "customer"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("search/", views.CustomerListView.as_view(), name="customer-list"),
    path("customer-create/", views.CustomerCreateView.as_view(), name="cust-create"),
    path(
        "detail/<slug:slug>/",
        views.CustomerDetailView.as_view(),
        name="customer-detail",
    ),
    path(
        "update-account/<slug:slug>",
        views.CustomerUpdateView.as_view(),
        name="customer-update",
    ),
]
