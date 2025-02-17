

```markdown
# Diabetes Progression Prediction

This project uses **Linear Regression** to predict the progression of diabetes based on various health metrics. It utilizes a dataset containing features such as age, sex, BMI, blood pressure, and others. The goal is to assess the model's ability to predict the progression of diabetes over time.

## Dataset

The dataset used in this project is the **Diabetes dataset** from **scikit-learn**. It includes the following features:

- **age**: Age of the patient
- **sex**: Sex of the patient
- **bmi**: Body Mass Index
- **bp**: Blood pressure
- **s1, s2, s3, s4, s5, s6**: Various blood serum measurements

## Steps

1. **Data Preprocessing**: The dataset is loaded, and features are selected for training the model.
2. **Model Training**: A **Linear Regression** model is trained using the training dataset.
3. **Model Evaluation**: The model is evaluated using **Root Mean Squared Error (RMSE)**.

## Installation

To run this project, you'll need the following libraries:
- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`

You can install them using pip:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Running the Project

Once the dependencies are installed, you can run the Python script to train the model and evaluate its performance. The RMSE score will be printed, and a plot comparing the actual and predicted diabetes progression will be displayed.

## Results

The model’s performance will be evaluated using **Root Mean Squared Error (RMSE)**, which gives an idea of how well the model can predict diabetes progression.
