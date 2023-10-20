FROM python:3.8
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
CMD streamlit run prediction_web_app.py
        