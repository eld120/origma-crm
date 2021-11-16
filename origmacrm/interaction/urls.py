from django.urls import path

from .views import NewInteractionView

app_name = "interaction"

urlpatterns = [path("", NewInteractionView.as_view(), name="new-interaction")]
