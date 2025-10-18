🚲 Vélib’ Station Availability Forecasting in Paris

This project explores the availability of Vélib’ shared bikes in Paris to analyze station usage patterns and build predictive models for future bike availability.
As someone who now commutes everywhere in Paris by bike instead of using the Navigo pass, I was personally motivated to understand which stations are most available and when they tend to be full or empty.

⸻

📜 Project Overview

The Vélib’ system provides real-time data on bike stations across Paris, including:
	•	Station ID and name
	•	Number of available bikes
	•	Number of free docks
	•	Bike types (mechanical, electric)
	•	Timestamp of last update
	•	Geographic coordinates

Using these features, this project aims to:
	1.	Analyze the usage patterns of Vélib’ stations.
	2.	Identify the busiest or emptiest stations throughout the day.
	3.	Build predictive models to forecast station availability over time.
	4.	Explore the temporal and spatial behavior of the Paris bike network.

⸻

🚀 Approach Summary

1️⃣ Data Analysis (EDA)
	•	Study the distribution of available bikes per station.
	•	Identify peak hours and daily trends.
	•	Detect spatial differences between central and suburban stations.

2️⃣ Feature Engineering
	•	Extract features from timestamp: hour, weekday, weekend indicator.
	•	Calculate variation in bike count between consecutive timestamps.
	•	Aggregate statistics by hour and station.

3️⃣ Modeling

Two modeling directions are explored:
	•	Machine Learning (Scikit-Learn):
Regression models such as Random Forest and Gradient Boosting to predict bike count.
	•	Deep Learning (PyTorch):
A simple LSTM (Long Short-Term Memory) neural network to forecast future availability based on past values.

4️⃣ Evaluation
	•	Metrics: RMSE (Root Mean Squared Error), MAE (Mean Absolute Error).
	•	Compare performance between classical ML and deep learning approaches.

⸻

🎯 Project Objectives
	•	🧠 Analytical Goal: Understand bike station dynamics in Paris.
	•	🚴‍♂️ Personal Motivation: I stopped using the Navigo pass and now move everywhere by bike — I want to know when and where stations tend to be full or empty.
	•	🔮 Technical Goal: Develop a predictive model for future bike availability using Scikit-Learn and PyTorch.

⸻

🔧 Data Processing & Methodology

📂 Data Source
Open Data Paris — Vélib’ “Disponibilité en temps réel” CSV dataset.

🧹 Data Cleaning
	•	Handle missing or inconsistent values.
	•	Normalize station names and identifiers.
	•	Parse timestamps into proper datetime format.

🧠 Feature Engineering
	•	Extract time-based features (hour, day of week, weekend flag).
	•	Compute deltas of bike availability between consecutive updates.
	•	Aggregate data by station and hour for smoother temporal patterns.

⚙️ Modeling
	•	Split data chronologically into train and test sets.
	•	Use Random Forest Regressor as baseline predictive model.
	•	Implement an LSTM neural network (PyTorch) for sequence forecasting of bike availability.

⸻

🛠️ Technology Stack
	•	Python for data analysis and modeling.
	•	Pandas & NumPy for data manipulation.
	•	Matplotlib & Seaborn for visualization.
	•	Scikit-Learn for classical machine learning.
	•	PyTorch for deep learning (time series forecasting).
	•	Jupyter Notebook for analysis and documentation.

⸻

📈 Expected Outcomes
	•	Clear visualizations of bike availability by station and time of day.
	•	Predictive models capable of estimating bike availability for the next hour.
	•	Identification of stations most prone to being full or empty during rush hours.
	•	A reproducible and well-structured end-to-end data science project.

⸻

📊 Files & Notebooks
	•	velib-disponibilite-en-temps-reel.csv: Open Data Paris dataset.
	•	VelibAnalysis.ipynb: Data cleaning and exploratory analysis.
	•	VelibPrediction.ipynb: Modeling with Scikit-Learn and PyTorch.
