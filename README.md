# 🌦️ Weather Forecast Dashboard

A Streamlit-based interactive web application that allows users to upload weather data in CSV format and receive a **30-day forecast** using **Facebook Prophet**, along with trend and seasonality analysis, interactive plots, and downloadable predictions.

---

## 🚀 Features

* 📤 Upload weather data (CSV)
* 📈 Automatically detects numeric columns for forecasting
* 📊 Calculates and displays key statistics (max, min, average)
* 🧠 Uses Prophet model for 30-day time series forecasting
* 📅 Interactive forecast plot with actual values
* 🔄 Trend and seasonality visualization
* 📥 Option to download forecast data as CSV

---

## 🛠️ Technologies Used

* [Streamlit](https://streamlit.io/) – For building the interactive dashboard
* [Pandas](https://pandas.pydata.org/) – For data manipulation
* [Prophet](https://facebook.github.io/prophet/) – For time series forecasting
* [Plotly](https://plotly.com/python/) – For interactive visualizations

---

## 📂 How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/weather-forecast-dashboard.git
   cd weather-forecast-dashboard
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Upload your CSV file. Make sure it contains a `date` column (or `last_updated_epoch`) and at least one numeric column (e.g., `temperature_celsius`).

---

## 📋 CSV Format Example

| date       | temperature\_celsius |
| ---------- | -------------------- |
| 2024-01-01 | 21.5                 |
| 2024-01-02 | 22.0                 |
| ...        | ...                  |

* `date` or `last_updated_epoch` will be used for the time axis.
* One numeric column is required for forecasting.

---

## 📦 Output

After processing, you'll get:

* 📉 Forecast plot (actual + predicted)
* 📊 Seasonality and trend decomposition
* 📥 Downloadable CSV of forecasted data with `yhat`, `yhat_lower`, and `yhat_upper`


## ✨ Acknowledgments

* Built using [Streamlit](https://streamlit.io/)
* Forecasting powered by [Facebook Prophet](https://facebook.github.io/prophet/)
* Visuals by [Plotly](https://plotly.com/)

---
