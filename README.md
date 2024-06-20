# Ethics Classifier

Welcome to Ethics Classifier, an application that predicts whether a given statement is ethical or unethical based on its textual content. This repository contains the source code for the application built using Python, Flask, and Scikit-learn.

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [License](#license)

## Introduction

Ethics Classifier uses a machine learning model based on logistic regression to classify statements as ethical or unethical. The model is trained on a dataset of labeled statements, leveraging TF-IDF vectorization for feature extraction and logistic regression for classification.

The application provides a simple web interface where users can input a statement, and the model predicts its ethicality. It's built with Python Flask for backend development and incorporates HTML and CSS for the frontend.

## Technologies Used

- **Python**: Programming language used for backend logic and machine learning model development.
- **Flask**: Micro web framework for Python used to build the web application and handle HTTP requests.
- **Pandas**: Python library for data manipulation and analysis, used here to preprocess the dataset.
- **Scikit-learn (sklearn)**: Python library for machine learning tasks, including logistic regression for classification and TF-IDF vectorization.
- **HTML/CSS**: Frontend technologies used to create the user interface for inputting statements and displaying prediction results.

## How It Works

1. **Dataset Loading and Preprocessing**:
   - The dataset (`alp.csv`) is loaded using Pandas, which contains statements labeled with their ethicality.
   - Text preprocessing steps (lowercasing, removal of punctuation, etc.) are assumed to have been applied beforehand.

2. **Feature Extraction**:
   - TF-IDF Vectorization is used to convert textual data into numerical features, capturing the importance of words in the statements.

3. **Model Training**:
   - The logistic regression model is trained on the TF-IDF transformed dataset to predict whether a statement is ethical (1) or unethical (0).

4. **Web Application**:
   - Flask is used to create the web application.
   - Users can access the application through a browser.
   - They can input a statement via a form, and upon submission, the model predicts its ethicality.
   - Results are displayed on a results page, indicating whether the statement is classified as ethical or unethical.

## Setup Instructions

To run the Ethics Classifier locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/SathwikLokam/Ethical-Sentence-Evaluator/
   cd Ethical-Sentence-Evaluator
2. Run the application
   cd /Ethical-Sentence-Evaluator/
   ./Scripts/activate
   python -m app.py
   
