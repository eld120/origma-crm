# from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from .models import Interaction

# Create your views here.

User = get_user_model()


class NewInteractionView(LoginRequiredMixin, CreateView):
    model = Interaction
    fields = [
        "date",
        "contact",
        "business",
        "notes",
        "initiative",
        "involved_contacts",
        "expected_sales",
        "realized_sales",
    ]


class CustomerDashboardView(LoginRequiredMixin, TemplateView):
    pass
