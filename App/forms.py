from django import forms

class NTNSearchForm(forms.Form):
    ntn_number = forms.CharField(max_length=50, required=True, label='Enter Supplier NTN Number')
