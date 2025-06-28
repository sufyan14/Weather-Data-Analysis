import streamlit as st
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_components_plotly
import plotly.express as px

# Page configuration
st.set_page_config(page_title="🌦️ Weather Forecast Dashboard", layout="wide")

# App title and description
st.title("🌦️ Weather Temperature Forecast Dashboard")
st.markdown("Upload weather data and get a 30-day forecast with trend analysis and insights.")

# File uploader
uploaded_file = st.file_uploader("📤 Upload your weather data CSV", type=["csv"])

if uploaded_file:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Handle datetime: prefer 'date', fallback to 'last_updated_epoch'
    if 'date' in df.columns:
        df['ds'] = pd.to_datetime(df['date'])
    elif 'last_updated_epoch' in df.columns:
        df['ds'] = pd.to_datetime(df['last_updated_epoch'], unit='s')
    else:
        st.error("❌ No valid datetime column found. Please include 'date' or 'last_updated_epoch'.")
        st.stop()

    # Detect numeric columns and let user select target for forecasting
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if not numeric_cols:
        st.error("❌ No numeric column found to forecast.")
        st.stop()

    default_col = 'temperature_celsius' if 'temperature_celsius' in numeric_cols else numeric_cols[0]
    target_col = st.selectbox("📌 Select column to forecast:", options=numeric_cols, index=numeric_cols.index(default_col))
    df['y'] = df[target_col]

    # Filter only required columns
    df = df[['ds', 'y']].dropna()

    # Train Prophet model
    model = Prophet()
    model.fit(df)

    # Create future dataframe for 30 days ahead
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    # Layout: Display statistics
    st.subheader("📊 Key Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📈 Max", f"{df['y'].max():.2f}")
    with col2:
        st.metric("📉 Min", f"{df['y'].min():.2f}")
    with col3:
        st.metric("📊 Average", f"{df['y'].mean():.2f}")

    # Plot forecast with actuals
    st.subheader("📅 Forecast Plot")
    fig1 = px.line(forecast, x="ds", y="yhat", title=f"Predicted {target_col} for Next 30 Days", labels={"ds": "Date", "yhat": target_col})
    fig1.add_scatter(x=df["ds"], y=df["y"], mode="markers", name="Actual", opacity=0.3)
    st.plotly_chart(fig1, use_container_width=True)

    # Trend and seasonality
    st.subheader("📈 Trend & Seasonality")
    fig2 = plot_components_plotly(model, forecast)
    st.plotly_chart(fig2, use_container_width=True)

    # Download forecast
    st.subheader("📥 Download Forecast Data")
    download_df = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    csv = download_df.to_csv(index=False).encode()
    st.download_button(label="Download as CSV", data=csv, file_name='forecast.csv', mime='text/csv')
