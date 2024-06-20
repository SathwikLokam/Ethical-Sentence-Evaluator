from flask import Flask
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from flask import Flask, request, render_template

app = Flask(__name__)

# Step 1: Load and Explore the Dataset
# Load the dataset
dataset = pd.read_csv('./alp.csv')

# Step 2: Preprocess the Text Data (if necessary)
# For simplicity, assuming the dataset is already preprocessed (lowercase, no punctuation, etc.)

# Step 3: Feature Extraction
# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')

# Fit and transform the text data
X = vectorizer.fit_transform(dataset['Text'])
y = dataset['Ethical']

# Step 4: Model Training
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 5: Evaluation
# Predict on the test set and evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Flask routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        statement = request.form['statement']
        X_new = vectorizer.transform([statement])
        prediction = model.predict(X_new)[0]
        
        if prediction == 1:
            result = "Ethical"
        else:
            result = "Unethical"
        
        return render_template('result.html', statement=statement, result=result)

if __name__ == "__main__":
    app.run(debug=True)




app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/')
def index():
    return redirect(url_for('index.html'))

if __name__=='__main__':
    app.run()
