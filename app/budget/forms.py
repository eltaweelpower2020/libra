from django import forms
from .models import LibraBudget

class LibraBudgetform(forms.ModelForm):
    class Meta:
        model=LibraBudget
        # fields = "__all__"
        exclude = ('added_by',)
        # fields = {'facebook_password','facebook_email',}
        # fields = ['facebook_email','facebook_password',]
        