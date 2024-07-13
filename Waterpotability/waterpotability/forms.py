from django import forms

class WaterQualityForm(forms.Form):
    ph = forms.FloatField(label='pH')
    hardness = forms.FloatField(label='Hardness')
    solids = forms.FloatField(label='Solids')
    chloramines = forms.FloatField(label='Chloramines')
    sulfate = forms.FloatField(label='Sulfate')
    conductivity = forms.FloatField(label='Conductivity')
    organic_carbon = forms.FloatField(label='Organic Carbon')
    trihalomethanes = forms.FloatField(label='Trihalomethanes')
    turbidity = forms.FloatField(label='Turbidity')
