import streamlit as st
import pandas as pd
import pickle

def preprocessing_pipeline(df):
    #convert date to datetime format
    df['ds'] = pd.to_datetime(df['ds'])

    df['ds'] = df['Date'].dt.to_period('M')

    df['ds'] = df['Date'].dt.to_timestamp()

    return df


def load_model(category):
    with open(f'{category}_model.pkl', 'rb') as file:
        model, features = pickle.load(file)
    return model, features


def app():
    st.title('Sales Volume Forecasting')
    st.write('Select a Category of Product to Make Prediction')

    category = st.selectbox('Category', ['Accessories', 'Laptop', 'Smartphone', 'Tablet'])

    start_date = st.date_input('Start_date')
    end_date = st.date_input('end_date')

    df = pd.DataFrame({'ds': pd.date_range(start_date, end_date)})

    df = preprocessing_pipeline(df)

    model, features = load_model(category)

    prediction = model.prediction(df)

    predict_plot = prediction[['ds', 'yhat']]
    st.line_chart(predict_plot, x = 'ds', y ='yhat')
    
if __name__ == '__main__':
    app()