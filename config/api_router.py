from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from origmacrm.customer import views
from origmacrm.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

router.register(r"customers", views.CustomerViewSet)
router.register(r"addresses", views.AddressViewSet)

app_name = "api"
urlpatterns = router.urls
