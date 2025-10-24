# 🚲 Vélib Usage Time Series Analysis between Cité Universitaire and Dauphine

This project aims to analyze the Vélib bike-sharing system in Paris, focusing especially on two stations I use daily: Cité Universitaire and Université Paris Dauphine. The goal is to understand historical and real-time bike availability patterns, especially for electric bikes, and build predictive algorithms to recommend the best time for picking up and dropping off bikes.

## 📜 Project Overview

I use Vélib every day for commuting between Cité Universitaire and Dauphine. To optimize my commute, I analyze historical and real-time Vélib data to predict when electric bikes are likely to be available to pick up and when docks will be free to return bikes. This involves collecting time-series snapshots from the system over time.

## 🚀 Approach Summary

### Data Collection
- Automated periodic collection of real-time status from the Vélib API every 10 minutes.
- Storing snapshots of bike counts, availability, and station metadata with timestamps.

### Data Analysis
- Comparing distributions of mechanical vs electric bikes.
- Visualizing temporal patterns, hourly/daily usage trends, and dock occupancy rates.
- Identifying high-demand regions and temporal usage clusters.

### Feature Engineering
- Extracting time-based features (hour of day, day of week).
- Constructing lagged features for time series forecasting.
- Optionally including weather or event data for richer context.

### Modeling & Prediction
- Comparison of predictive models built with:
  - **Scikit-learn** (classical machine learning such as Random Forest and Gradient Boosting Regression).
  - **PyTorch** (deep learning recurrent networks such as LSTM and GRU).
- This comparison allows exploring the trade-offs between model complexity, interpretability, and forecasting accuracy.

## 🎯 Project Objectives

- Understand usage dynamics at Cité Universitaire and Dauphine stations.
- Predict optimal time windows for picking up electric bikes.
- Predict optimal times for returning bikes to avoid full docks.
- Provide actionable and personalized recommendations to improve daily commutes.

## 🔧 Technology Stack

- **Python** with libraries such as Pandas, NumPy, Matplotlib, and Seaborn for data processing and visualization.
- **Requests** for API data fetching.
- **Scikit-learn** for classical machine learning models.
- **PyTorch** for deep learning sequence models.
- **Jupyter Notebook** for exploratory analysis and documentation.

## 📈 Impact

- Enhanced personal commute planning with data-driven insights.
- Demonstration of time series forecasting approaches for urban mobility.
- Potential framework applicable to other bike-sharing or shared micro-mobility systems.

## 📂 Project Files

- `velib_historico.csv`: Consolidated time-stamped snapshots of Vélib station status.
- `Velib_TimeSeries_Analysis.ipynb`: Notebook containing data exploration, feature engineering, and predictive modeling.
- `DataCollectionScript.py`: Python script to automate periodic API data collection.

---

Feel free to reach out if you want help including example codes or usage instructions. If you find this helpful, consider starring the project! ⭐

