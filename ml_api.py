#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 11:36:01 2025

@author: satyamgajjar
"""

from fastapi import FastAPI #helps you build APIs easily.
from pydantic import BaseModel #checks that the data sent by users is valid and in correct format.
import pickle #loads your saved machine learning model.
import json #helps convert text to dictionary.

app = FastAPI() #This is like turning on your server.

class model_input(BaseModel):
    
    Pregnancies : int	
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age: int
    
    
#loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
 
@app.post('/diabetes_prediction')
def diabetes_pred(input_parametes: model_input):
    
    input_data = input_parametes.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
     
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The person is not Diabetic'
    
    else: 
        return 'The person is Diabetic'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











