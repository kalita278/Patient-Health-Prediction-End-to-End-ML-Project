
import pickle
import streamlit as st
import numpy as np
import pandas as pd
from src.pipeline.prediction_pipeline import PredictionPipeline
import pymysql

preprocessor =pickle.load(open('artifacts\data_transformation\preprocessor.pkl', 'rb'))
model = pickle.load(open('artifacts\model_trainer\model.pkl', 'rb'))
a = pymysql.connect(user='root',host='127.0.0.1',passwd='mrinal',db='patient_condition')
cur = a.cursor()
                                
                                
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
        if prediction[0] == "Normal":
            cur.execute('insert into Normal(P_incidence,P_tilt,L_angle,S_slope,P_radius,S_Degree,Class) values(%s,%s,%s,%s,%s,%s,%s)',(P_incidence,P_tilt,L_angle,S_slope,P_radius,S_Degree,prediction[0]))
            a.commit()
            a.close()
        elif prediction[0] == 'Type_H':
            cur.execute('insert into Type_H(P_incidence,P_tilt,L_angle,S_slope,P_radius,S_Degree,Class) values(%s,%s,%s,%s,%s,%s,%s)',(P_incidence,P_tilt,L_angle,S_slope,P_radius,S_Degree,prediction[0]))
            a.commit()
            a.close()
        else:
            cur.execute('insert into Type_S(P_incidence,P_tilt,L_angle,S_slope,P_radius,S_Degree,Class) values(%s,%s,%s,%s,%s,%s,%s)',(P_incidence,P_tilt,L_angle,S_slope,P_radius,S_Degree,prediction[0]))
            a.commit()
            a.close()

    st.success(prediction[0])
    
if __name__ == '__main__':
    main()
    