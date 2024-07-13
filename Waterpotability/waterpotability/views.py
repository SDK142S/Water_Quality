from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

# Load and preprocess data
df = pd.read_csv('water_quality_data.csv')
X = df.drop('Potability', axis=1)
y = df['Potability']
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.1, random_state=52)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

def index(request):
    return render(request, 'waterpotability/index.html')

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
        result = "Potable" if prediction == 1 else "Not Potable"
        return render(request, 'waterpotability/result.html', {'result': result})
    return HttpResponse("Invalid request method.", status=405)
