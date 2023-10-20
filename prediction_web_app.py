
import pickle
import streamlit as st
import numpy as np
import pandas as pd
from src.pipeline.prediction_pipeline import PredictionPipeline

preprocessor =pickle.load(open('artifacts\data_transformation\preprocessor.pkl', 'rb'))
model = pickle.load(open('artifacts\model_trainer\model.pkl', 'rb'))
                                
                                
def main():
    st.title("Patient Condition Prediction")
    st.header("Enter the value of the following parameters:")
    P_incidence	 = st.number_input("Enter the value of P_incidence")
    P_tilt	 = st.number_input("Enter the value of P_tilt")
    L_angle	 = st.number_input("Enter the value of L_angle")
    S_slope	 = st.number_input("Enter the value of S_slope")
    P_radius = st.number_input("Enter the value of P_radius")
    S_Degree = st.number_input("Enter the value of S_degree")

    data = [[P_incidence,P_tilt,L_angle,S_slope,P_radius,S_Degree]]
    df = pd.DataFrame(data, columns=['P_incidence','P_tilt','L_angle','S_slope','P_radius','S_Degree'])
    
    
    prediction = ' '
    
    if st.button('Predict Patient condition'):
        obj = PredictionPipeline()
        prediction=obj.predict(data=df)
        
    st.success(prediction[0])
    
if __name__ == '__main__':
    main()
    