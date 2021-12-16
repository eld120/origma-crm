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
    path("create-address/", views.AddressCreateView.as_view(), name="address-create"),
    path(
        "test-customer-create/", views.test_customer_create, name="test-customer-create"
    ),
    path("customer-test/", views.customer_create, name="customer-test"),
    path(
        "test-customer-update/<slug:slug>",
        views.test_customer_update,
        name="test-customer-update",
    ),
    path("test-address-create/", views.test_address_create, name="test-address-create"),
    path(
        "test-address-update/<int:pk>",
        views.test_address_update,
        name="test-address-update",
    ),
]
