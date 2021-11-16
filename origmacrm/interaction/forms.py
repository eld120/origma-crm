from django import forms

from .models import Interaction


class InteractionForm(forms.ModelForm):
    """form to handle the maintenance of all customer interactions"""

    model = Interaction
