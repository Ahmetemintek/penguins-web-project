# Penguins Web Project

## Introduction
This repository contains a Streamlit web application that predicts the species of penguins based on their input parameters, including bill length, bill width, flipper length, body mass, sex, and island.

## Files in Repository
- **Procfile:** Configuration file used to run the Streamlit web app on hosting platforms like Heroku.
- **class_model.pkl:** Pickled machine learning model file used for penguin species prediction.
- **penguins_app.py:** Main Python script containing the Streamlit web application code.
- **penguins_cleaned.csv:** Cleaned and preprocessed training data for training the machine learning model.
- **setup.sh:** Shell script file for setting up the necessary environment or dependencies.

## How to Use
1. Clone or download this repository to your local machine.
2. Ensure you have Python and necessary libraries installed (requirements specified in requirements.txt).
3. Run the Streamlit app using the command: `streamlit run penguins_app.py`
4. Access the web app in your browser using the provided URL (usually starts with http://localhost).

## Notes
- The prediction model (`class_model.pkl`) is based on machine learning algorithms trained on the penguin dataset (`penguins_cleaned.csv`).
- The Procfile is used to configure the app for deployment on hosting platforms like Heroku.
- Additional setup or dependencies can be managed using the setup.sh script.

Feel free to explore and use the app for predicting penguin species!

