# Machine Learning API Implementation

A Python script that demonstrates how to interact with a machine learning prediction API using HTTP requests.  
This project shows how to send input data to a locally hosted model API and receive prediction results in JSON format.

## Table of Contents
1. Overview
2. Problem Statement
3. API Description
4. Input Data Format
5. How the API Call Works
6. How to Run the Script
7. Output
8. Technologies Used
9. Use Cases
10. Future Improvements
11. Author

## Overview
This project demonstrates how a client application communicates with a machine learning model deployed as an API.

The script sends structured input data to a prediction endpoint and receives the model output as a response.  
It represents a common real world workflow used in machine learning deployment and system integration.

## Problem Statement
Given patient health related parameters, send the data to a machine learning API and retrieve a diabetes prediction result.

The goal is to simulate real world model consumption rather than model training.

## API Description
The API is hosted locally and exposes a prediction endpoint.

Endpoint URL:
http://127.0.0.1:8000/diabetes_prediction

Request Method:
POST

The API expects input data in JSON format and returns a prediction response.

## Input Data Format
The input data represents patient medical information.

Example fields include:
1. Pregnancies
2. Glucose
3. BloodPressure
4. SkinThickness
5. Insulin
6. BMI
7. DiabetesPedigreeFunction
8. Age

All values are sent as key value pairs in JSON format.

## How the API Call Works
1. Input data is defined as a Python dictionary
2. The dictionary is converted to JSON format
3. A POST request is sent to the API endpoint
4. The API processes the input using a trained ML model
5. The prediction response is returned and printed

## How to Run the Script
1. Ensure the machine learning API server is running locally
2. Verify the endpoint URL and port number
3. Install required libraries if not already installed
4. Run the Python script from terminal or IDE

Example command:
python api_implementation.py

## Output
The script prints the API response returned by the model.

The response typically contains:
1. Prediction result
2. Model output message
3. Status information

## Technologies Used
1. Python
2. Requests library
3. JSON
4. REST API
5. Machine Learning Model API

## Use Cases
1. Testing deployed machine learning models
2. Client side API integration
3. Model inference validation
4. Backend to backend communication
5. Production readiness checks

## Future Improvements
1. Add error handling for API failures
2. Validate input data before sending
3. Handle JSON responses properly
4. Add logging instead of print statements
5. Convert this into a reusable API client module

## Author
Satyam Gajjar
