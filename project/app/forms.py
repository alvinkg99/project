from django import forms


class YourModelSearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, required=False)