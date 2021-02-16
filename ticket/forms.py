from django import forms

class TicketForm(forms.Form):
    name = forms.CharField(label='Enter your Name', max_length=200)
