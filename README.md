# Machine Learning Practice Repository

This repository is dedicated to practicing key concepts from the **Machine Learning** course by Andrew Ng on Coursera. Each section focuses on solving problems related to the main topics covered in the course.

## Topics

- [x] Linear Regression
- [ ] Logistic Regression
- [ ] Neural Networks
- [ ] Unsupervised Learning
- [ ] Anomaly Detection
- [ ] Recommender Systems

---

## Folder Structure

```
machine-learning-practice/
├── data
│ ├── raw
│ ├── processed
│ └── README.md # Notes on datasets and preprocessing
|
├── notebooks
│ └── ... # Organized by topic
|
├── src
│ ├── preprocessing.py
│ ├── models.py # Code for building and training models
│ ├── utils.py
│ └── README.md # Notes on how to use scripts in `src/`
|
├── results/ # Outputs of experiments (e.g., graphs, logs, model weights)
│ └── ... # Organized by topic
|
├── reports/ # Summary reports for each problem or experiment
│ └── ... # Organized by topic
|
├── tests/ # Unit tests for code in `src/`
```

---

## Linear Regression

### Overview

Linear regression is a supervised learning algorithm used for predicting a target variable (y) based on a single feature (x) or multiple features (X). The goal is to minimize the error between the predicted and actual values by fitting a straight line.

### Current Problem: Predicting Housing Prices

In this problem, we use a simple linear regression model to predict house prices based on one feature:

- **Feature (x):** Average number of rooms (`RM`)
- **Target (y):** House price (`PRICE`)

### Steps

1. **Understand the Data:**

   - Use the Boston Housing dataset (`RM` vs. `PRICE`).

2. **Build the Model:**

   - Train a simple linear regression model using one feature (`RM`).

3. **Evaluate the Model:**

   - Calculate metrics like Mean Squared Error (MSE).
   - Visualize the results with a scatterplot and regression line.

4. **Experiment:**
   - Try another feature like `LSTAT` to see how it affects predictions.
