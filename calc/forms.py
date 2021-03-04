from django import forms

class CalculatorForm(forms.Form):
    number_one = forms.FloatField(widget=forms.NumberInput)
    number_two = forms.FloatField(widget=forms.NumberInput)
    operator = forms.ChoiceField(choices=[('+', '+'), ('-', '-'), ('*', '*'), ('/', '/')])