import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Penguin Prediction Appp
This app predicts the **Palmer Penguins** species

Data obtained from the [palmer penguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.

""")
st.sidebar.header("User Input Features")

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

# uploading data
uploaded_file= st.sidebar.file_uploader("Upload your csv file", type=["csv"])
if uploaded_file is not None:
    input_df= pd.read_csv(uploaded_file)
else:
    def user_input_features(): #manuel selecting if no uploaded file
        island= st.sidebar.selectbox("Island", ("Biscoe", "Dream", "Torgersen"))
        sex= st.sidebar.selectbox("Sex", ("male", "female"))
        bill_length_mm= st.sidebar.slider("Bill lenght (mm)", 32.1, 59.6, 43.9)
        bill_depth_mm= st.sidebar.slider("Bill depth (mm)", 13.1, 21.5, 17.2)
        flipper_length_mm= st.sidebar.slider("Flipper length (mm)", 172.0, 231.0, 201.0)
        body_mass_g= st.sidebar.slider("Boddy mass (g)", 2700.0, 6300.0, 4207.0)
        data = {"island": island,
                "sex":sex,
                "bill_length_mm": bill_length_mm,
                "bill_depth_mm": bill_depth_mm,
                "flipper_length_mm": flipper_length_mm,
                "body_mass_g": body_mass_g}
        features= pd.DataFrame(data, index=[0])
        return features
    input_df= user_input_features()

# merging the original dataframe with the input(input_df)
pen_raw= pd.read_csv("/Users/ahmetemintek/Desktop/penguins-project/penguins_cleaned.csv")
penguins= pen_raw.drop(columns=["species"])
df= pd.concat([input_df, penguins], axis=0) #user inputs will be on the first

# encoding df
encode= ["sex", "island"]
for col in encode:
    df= pd.concat([df, pd.get_dummies(df[col], prefix=col)], axis=1)
    del df[col]
df= df[:1] #we choose only the first row for the prediction

# showing the user inputs
if uploaded_file is not None:
    st.write(df)
else:
    st.write("Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).")
    st.write(df)

# reading the model from the saved .pkl file
load_model= pickle.load(open("class_model.pkl", "rb"))

# prediction
pred= load_model.predict(df)
pred_proba= load_model.predict_proba(df)

# displaying the results
st.subheader("Target Values")
penguins_species= np.array(["Adelie", "Chinstrap", "Gentoo"])
st.write(penguins_species)

st.subheader("Prediction")
penguins_species= np.array(["Adelie", "Chinstrap", "Gentoo"])
st.write(penguins_species[pred])

st.subheader("Prediction Probability")
st.write(pred_proba)
