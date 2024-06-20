<!-- templates/introduction.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Introduction to Ethics Classifier</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f0f0f0;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #ffffff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333333;
        }
        p {
            line-height: 1.6;
            color: #666666;
        }
        .highlight {
            font-weight: bold;
            color: #007bff;
        }
        .features {
            margin-top: 20px;
        }
        .features h3 {
            color: #333333;
        }
        .features ul {
            list-style-type: disc;
            margin-left: 20px;
            color: #666666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Introduction to Ethics Classifier</h1>
        <p>Welcome to the Ethics Classifier application!</p>
        
        <div class="features">
            <h3>How It Works:</h3>
            <p>The Ethics Classifier is built using several key technologies and methodologies:</p>
            <ul>
                <li><span class="highlight">Python Flask Framework:</span> A micro web framework used to develop web applications in Python, providing routing, template rendering, and more.</li>
                <li><span class="highlight">Pandas:</span> A powerful data analysis and manipulation library for Python, utilized here to load and preprocess the dataset.</li>
                <li><span class="highlight">Scikit-learn (sklearn):</span> A machine learning library in Python that includes various algorithms for classification, regression, clustering, and more.</li>
                <li><span class="highlight">Logistic Regression:</span> A statistical model used for binary classification tasks, trained on a labeled dataset of statements to predict their ethicality.</li>
                <li><span class="highlight">TF-IDF Vectorization:</span> Term Frequency-Inverse Document Frequency is used to convert textual data into numerical features, capturing the importance of words in the statements.</li>
                <li><span class="highlight">HTML and CSS:</span> Front-end technologies used to create a user-friendly interface for inputting statements and displaying prediction results.</li>
            </ul>
        </div>
        
        <p>The application allows users to input a statement and predicts whether it is <span class="highlight">ethical</span> or <span class="highlight">unethical</span> based on its content.</p>
        
        <p>Explore the various functionalities and enjoy using the Ethics Classifier!</p>
    </div>
</body>
</html>
