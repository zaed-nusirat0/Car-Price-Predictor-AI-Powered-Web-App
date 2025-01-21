# Car Price Prediction Project

This project focuses on predicting car prices using machine learning techniques. The dataset used contains various features related to cars, such as make, model, type, origin, drivetrain, MSRP, invoice, engine size, cylinders, horsepower, MPG (city and highway), weight, wheelbase, and length.

---

## Key Features

- **Data Exploration**: The dataset is explored using various Python libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Plotly. The data is cleaned and preprocessed to handle missing values, duplicates, and data type conversions.
- **Data Visualization**: Visualizations are created to understand the distribution of missing values, unique values, and other statistical properties of the dataset.
- **Machine Learning Models**: The project uses several machine learning models, including `RandomForestRegressor`, `GradientBoostingRegressor`, and `AdaBoostRegressor`, to predict car prices. The models are evaluated using metrics like R² score and mean squared error.
- **Data Preprocessing**: The dataset undergoes preprocessing steps such as label encoding, ordinal encoding, and feature transformation to prepare it for machine learning.
- **Model Pipeline**: A pipeline is created using `ColumnTransformer` and `Pipeline` from `sklearn` to streamline the preprocessing and modeling steps.

---

## Libraries Used

- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Matplotlib & Seaborn**: For data visualization.
- **Plotly**: For interactive visualizations.
- **Scikit-learn**: For machine learning models and evaluation metrics.

---

## Steps

1. **Data Loading**: The dataset is loaded from a CSV file.
2. **Data Cleaning**: Missing values and duplicates are handled. String values are converted to numeric where necessary.
3. **Exploratory Data Analysis (EDA)**: The dataset is analyzed to understand its structure, distribution, and relationships between features.
4. **Model Training**: Multiple regression models are trained and evaluated.
5. **Model Evaluation**: The performance of the models is assessed using R² score and mean squared error.

---

## Key Insights

- The dataset contains **432 rows** and **15 features**.
- Missing values are handled by dropping rows with missing data.
- The target variable is the car's price (**MSRP**), which is predicted using various features.
- The project demonstrates the use of ensemble methods for regression tasks.

---

# Car Price Prediction App

This is a Flask-based web application for predicting car prices using a pre-trained machine learning model.

## Features

- Predict car prices based on various features such as Make, Type, Origin, DriveTrain, MSRP, EngineSize, Cylinders, Horsepower, Weight, Wheelbase, and Length.
- Simple and intuitive user interface.

---

## How to Run

### Using Docker

1. Pull the Docker image from Docker Hub:
   ```bash
   docker pull zaidtech/car_price_prediction

## Installation

### Using Docker

1. Pull the Docker image from Docker Hub:

   ```bash
   docker pull zaidtech/car_price_prediction

   docker run -p 8000:8000 zaidtech/car_price_prediction

   Run the Docker container:


Access the application at http://localhost:8000.

## Usage

1. Navigate to the home page.
2. Fill in the car details in the input form.
3. Submit the form to get the predicted car price.
