import re
import os
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')

# Assuming clf.pkl and tfidf.pkl are in the same directory as utils.py
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CLF_PATH = os.path.join(CURRENT_DIR, 'clf.pkl')
TFIDF_PATH = os.path.join(CURRENT_DIR, 'tfidf.pkl')

# Load the pre-trained model and vectorizer
clf = joblib.load(CLF_PATH)
tfidf = joblib.load(TFIDF_PATH)
stop_words = set(stopwords.words('english'))
porter = PorterStemmer()

def clean_resume(resume_file):
    try:
        resume_text = resume_file.read().decode('utf-8')
    except UnicodeDecodeError:
        # Fallback to 'latin-1' encoding if UTF-8 decoding fails
        resume_text = resume_file.read().decode('latin-1')
    clean_text = re.sub(r'http\S+', '', resume_text)  # Remove URLs
    clean_text = re.sub(r'\W', ' ', clean_text)       # Remove non-word characters
    clean_text = re.sub(r'\s+', ' ', clean_text)      # Remove extra whitespaces
    clean_text = clean_text.lower()                   # Convert to lowercase
    
    # Tokenize and remove stopwords
    tokens = nltk.word_tokenize(clean_text)
    cleaned_tokens = [porter.stem(token) for token in tokens if token.isalpha() and token not in stop_words]
    cleaned_resume = ' '.join(cleaned_tokens)
    
    return cleaned_resume

def predict_category(cleaned_resume):
    input_features = tfidf.transform([cleaned_resume])
    prediction_id = clf.predict(input_features)[0]
    
    print(f"Prediction ID: {prediction_id}")
    # Mapping category IDs to category names
    category_mapping = {
        
        15: "Java Developer",
        23: "Testing",
        8: "DevOps Engineer",
        20: "Python Developer",
        24: "Web Designing",
        12: "HR",
        13: "Hadoop",
        3: "Blockchain",
        10: "ETL Developer",
        18: "Operations Manager",
        6: "Mechanical Engineer",
        22: "Sales",
        16: "Data Science ",
        1: "Arts",
        7: "Database",
        11: "Electrical Engineering",
        14: "Health and fitness",
        19: "PMO",
        4: "Business Analyst",
        9: "DotNet Developer",
        2: "Automation Testing",
        17: "Network Security Engineer",
        21: "SAP Developer",
        5: "Civil Engineer",
        0: "Advocate",
        # Add more categories as needed
    }
    
    predicted_category = category_mapping.get(prediction_id, "Unknown")
    return predicted_category
