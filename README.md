# ResumeClassifier
# ResumeClassifier

ResumeClassifier is a Django-based web application designed to predict job categories from resumes using machine learning techniques. This project emphasizes user privacy and security by ensuring that no user data is stored beyond the processing phase.

## Overview

ResumeClassifier leverages natural language processing (NLP) to analyze the content of resumes and classify them into predefined job categories. The application provides a secure environment where users can upload their resumes, which are then analyzed using machine learning models without storing any personal data.

## Features

- **Resume Upload**: Users can securely upload their resumes for classification.
- **Job Category Prediction**: The application predicts job categories based on the content of the resumes.
- **Privacy-Focused**: No user data is stored after processing, ensuring user privacy.

## NLP Techniques

The core of ResumeClassifier relies on the following NLP techniques:

- **Text Preprocessing**: Cleaning and preprocessing resume text using tokenization, stop-word removal, and stemming.
- **Feature Extraction**: Utilizing CountVectorizer from Scikit-learn to transform text data into numerical features suitable for machine learning models.
- **Machine Learning Models**: Employing supervised learning models such as Support Vector Machines (SVM) for classification tasks.

## Installation

To run ResumeClassifier locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/vvinayakkk/ResumeClassifier.git
