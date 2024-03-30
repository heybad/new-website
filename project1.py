from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the pre-trained model and data
model = LinearRegression()
df = pd.read_csv('data/agevsincome.csv')
x = df[['age', 'experience']].values
y = df[['income']].values
model.fit(x, y)

def agevsincome():
    if request.method == 'POST':
        age = float(request.form['age'])
        experience = float(request.form['experience'])
        predictionss = model.predict([[age, experience]])[0][0]
        return render_template('project1.html', prediction=predictionss)
    return render_template('project1.html', prediction=None)
