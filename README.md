# Water Potability Prediction System  

## Overview  
The **Water Potability Prediction System** is a machine learning-based web application designed to analyze water quality parameters and predict whether water is safe for human consumption. This project emphasizes the importance of public health by utilizing predictive analytics to identify unsafe water, aiding in timely corrective measures.  

## Features  
- User-friendly interface developed using **Django**.  
- Real-time predictions of water potability based on key quality parameters.  
- Integration of machine learning models to ensure high accuracy, precision, and recall.  
- Supports analysis of environmental factors such as:  
  - pH  
  - Hardness  
  - Solids  
  - Chloramines  
  - Sulfate  
  - Conductivity  
  - Organic Carbon  
  - Trihalomethanes  
  - Turbidity  

## Dataset  
The project utilizes a Kaggle dataset containing water quality data with the following attributes:  
- **pH**: Acidity/basicity of water.  
- **Hardness**: Calcium and magnesium ion concentration.  
- **Solids**: Total dissolved solids in water.  
- **Potability**: Binary classification indicating whether water is drinkable (1) or not (0).  

Dataset link: [Water Quality Dataset on Kaggle](https://www.kaggle.com/datasets/adityakadiwal/water-potability).  

## Machine Learning Models  
Several machine learning algorithms were explored to evaluate predictive performance, including:  
- Logistic Regression  
- Random Forest  
- Gradient Boosting  
- Support Vector Machines (SVM)  

The best-performing model was integrated into the Django application for live predictions.  

