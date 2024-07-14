from django import forms

class WaterQualityForm(forms.Form):
    ph = forms.FloatField(
        label='pH',
        widget=forms.NumberInput(attrs={'placeholder': '0.00 - 14.00'})
    )
    hardness = forms.FloatField(
        label='Hardness',
        widget=forms.NumberInput(attrs={'placeholder': '47.43 - 323.12'})
    )
    solids = forms.FloatField(
        label='Solids',
        widget=forms.NumberInput(attrs={'placeholder': '320.94 - 61227.20'})
    )
    chloramines = forms.FloatField(
        label='Chloramines',
        widget=forms.NumberInput(attrs={'placeholder': '0.35 - 13.13'})
    )
    sulfate = forms.FloatField(
        label='Sulfate',
        widget=forms.NumberInput(attrs={'placeholder': '129.00 - 481.03'})
    )
    conductivity = forms.FloatField(
        label='Conductivity',
        widget=forms.NumberInput(attrs={'placeholder': '181.48 - 753.34'})
    )
    organic_carbon = forms.FloatField(
        label='Organic Carbon',
        widget=forms.NumberInput(attrs={'placeholder': '2.20 - 28.30'})
    )
    trihalomethanes = forms.FloatField(
        label='Trihalomethanes',
        widget=forms.NumberInput(attrs={'placeholder': '0.74 - 124.00'})
    )
    turbidity = forms.FloatField(
        label='Turbidity',
        widget=forms.NumberInput(attrs={'placeholder': '1.45 - 6.74'})
    )
