PCOS Diet Recommendation System
  This project aims to build a personalized diet recommendation system for patients with Polycystic Ovary Syndrome (PCOS). The system recommends diets based on various symptoms of PCOS, including obesity, insulin resistance, hormonal imbalance, menstrual issues, skin and hair problems, and ovulation problems.
Project Overview
  This system uses machine learning to predict the symptoms of PCOS based on user input and recommends relevant diets using the Spoonacular API. The system was built using Random Forest Classifier with a multi-label classification approach to predict multiple symptoms simultaneously. The project includes a user-friendly web interface using Streamlit, allowing users to input their health data and receive personalized dietary recommendations.
Key Features
  Symptom Prediction: Predicts PCOS symptoms based on user input (e.g., BMI, skin darkening, cycle length, etc.)
  Diet Recommendations: Provides diet recommendations based on the predicted symptoms.
  Real-time Recipe Fetching: Fetches recipes using the Spoonacular API for the recommended diet.
  Multi-label Classification: Uses a multi-label classification model to predict multiple symptoms simultaneously.
Technologies Used
  Python: Primary programming language
  Scikit-Learn: For machine learning and model training
  Streamlit: For building the web interface
  Spoonacular API: For fetching diet recommendations
  Joblib: For model persistence (saving and loading the trained model)
Model Training and Evaluation
  Data Preprocessing: The dataset was cleaned and prepared with features like BMI, cycle length, and skin darkening (for example) to predict the symptoms.
  Model: A Random Forest Classifier was used with MultiOutputClassifier for multi-label classification.
  Metrics: Model evaluation was performed using Hamming Loss and Macro F1 Score.
  Hamming Loss: Measures the average number of labels that are incorrectly predicted.
  F1 Score (Macro): The harmonic mean of precision and recall, averaged across all classes.
How to Use
  Input Symptoms: Enter your health data (e.g., BMI, cycle length, skin darkening, etc.) on the Streamlit app interface.
  Receive Diet Recommendations: The app will display recommended diets and fetch related recipes using the Spoonacular API.
  Adjust Inputs: Modify the input data to explore different recommendations.
Model Details
  Random Forest Classifier: The model was trained using a Random Forest Classifier to predict multiple symptoms at once.
  Cross-validation: The model performance was validated using cross-validation to ensure robustness and generalization.
  Hyperparameter Tuning: We used grid search to tune hyperparameters such as the number of trees, tree depth, and minimum samples to split or leaf nodes.
  
Future Enhancements
  Personalized Meal Plans: Introduce more advanced meal planning based on preferences like vegetarian or lactose intolerant.
  Real-time Monitoring: Integrate wearable health devices for real-time tracking of health metrics.
  User Feedback Loop: Add a feedback system to dynamically adjust diet recommendations based on user experiences.
