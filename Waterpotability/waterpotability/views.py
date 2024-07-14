from django.shortcuts import render
from django.http import HttpResponse
from .forms import WaterQualityForm
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

# Load and preprocess data
df = pd.read_csv('water_quality_data.csv')
X = df.drop('Potability', axis=1)
y = df['Potability']
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)
scaler = StandardScaler()
X_res = scaler.fit_transform(X_res)
model = RandomForestClassifier(random_state=42)
model.fit(X_res, y_res)

def index(request):
    if request.method == 'POST':
        form = WaterQualityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            features = [
                data['ph'],
                data['hardness'],
                data['solids'],
                data['chloramines'],
                data['sulfate'],
                data['conductivity'],
                data['organic_carbon'],
                data['trihalomethanes'],
                data['turbidity']
            ]
            features = scaler.transform([features])
            prediction = model.predict(features)[0]
            result = "Potable" if prediction == 1 else "Not Potable"
            return render(request, 'waterpotability/result.html', {'result': result})
        else:
            return render(request, 'waterpotability/index.html', {'form': form})
    else:
        form = WaterQualityForm()
        return render(request, 'waterpotability/index.html', {'form': form})

# Add the predict view function here
def predict(request):
    if request.method == 'POST':
        features = [
            float(request.POST['ph']),
            float(request.POST['hardness']),
            float(request.POST['solids']),
            float(request.POST['chloramines']),
            float(request.POST['sulfate']),
            float(request.POST['conductivity']),
            float(request.POST['organic_carbon']),
            float(request.POST['trihalomethanes']),
            float(request.POST['turbidity'])
        ]
        features = scaler.transform([features])
        prediction = model.predict(features)[0]
        result = "Water is safe to drink" if prediction == 1 else "Water is not safe to drink"
        return render(request, 'waterpotability/result.html', {'result': result})
    return HttpResponse("Invalid request method.", status=405)
