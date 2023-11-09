## Patient Health Prediction


**DOMAIN**: Medical

**CONTEXT:** Medical research university X is undergoing a deep research on patients with certain conditions. University has an internal AI team. Due  to  confidentiality  the  patient’s  details  and  the  conditions  are  masked  by  the  client  by  providing  different  datasets  to  the  AI  team  for developing a AIML model which can predict the condition of the patient depending on the received test results.

**DATA  DESCRIPTION**: The  data  consists  of  biomechanics  features  of  the  patients  according  to  their  current  conditions.  Each  patient  is represented in the data set by six biomechanics attributes derived from the shape and orientation of the condition to their body part. 

**PROJECT  OBJECTIVE**: To Demonstrate the ability to fetch, process and leverage data to generate useful predictions by training Supervised Learning algorithms.

**ATTRIBUTE INFORMATION:**
1. pelvic_incidence- P_incidence
2. pelvic_tilt numeric- P_tilt
3. lumbar_lordosis_angle- L_angle
4. sacral_slope- S_slope
5. pelvic_radius- P_radius
6. degree_spondylolisthesis- S_degree
7. class

**DATA PREPARATION AND EXPLORATION:**

Combined all three files to create a single file with all the relevant variables and perform the necessary data quality checks and cleaning. In data cleaning, identified the missing values/unexpected values and outliers in the dataset (if any) and impute that with the mean value. Also, make sure that data types of the variables are appropriate as required for our analysis.

**DATA ANALYSIS:**

Here, performed uni-variate, bivariate, and multivariate analysis of the dataset, for example, 5-point summary of the continuous variable, pair plot, joint plot, correlation plot, and boxplot to detect outliers.

**DATA PREPROCESSING:**

Encoded the target variable and scaled the independent variable using label encoder and standardscaler respectively.

**MODEL BUILDING, EVALUATION AND IMPROVEMENT:**

Used k nearest neighbour, SVC, Logistic regression, Naive Bayes, Decision Tree, Random Forest, Ada boost, and Gradient Boost algorithm to detect the patient condition and evaluate the model using confusion matrix, accuracy score, recall score, precision score, and f1 score. Further tunned the model using GridsearchCV and increased the accuracy of the model by almost ~5%.

## **MLOPS:**
Used mlops tools to version the model and data that becomes scalable and reproducible in the future.

## **MLOPS Tools:**
MLFlow, DVC, GIT, Dagshub

**MODEL DEPLOYMENT:**

**Web Application:** Streamlit

**Container:** Docker

**Cloud deployment:** GCP

**Dagshub Repository link:** https://dagshub.com/kalita278/Patient-Health-Prediction-End-to-End-ML-Project


### **How to use it**
To use this project, first clone the repo on your device using the command below:

git clone https://github.com/kalita278/Patient-Health-Prediction-End-to-End-ML-Project.git

## **Installation**
pip install -r requirements.txt

## **How to run the project**
1. Run: "streamlit run prediction_web_app.py" to get the localhost server link. 

2. Go to the browser and load  http://127.0.0.1:8501/
