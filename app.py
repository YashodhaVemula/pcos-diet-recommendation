import streamlit as st
import pandas as pd
import requests
from joblib import load

# Load the trained machine learning model
rf_model = load("rf_model.joblib")

# Define your Spoonacular API key
api_key = "6123f2cf2df64103a3e3bd775dfc5c05"


# Function to get diet recommendations based on the symptom type
def get_diet_recommendations(symptom_type, min_recipes=7):
    base_url = "https://api.spoonacular.com/recipes/complexSearch"

    params = {
        "apiKey": api_key,
        "number": 15  # Request more recipes to ensure at least 7 valid ones
    }

    if symptom_type == "Obesity":
        params.update({"diet": "low-calorie", "maxCalories": 500})
    elif symptom_type == "Insulin_Resistance":
        params.update({"diet": "low-carb", "query": "low glycemic"})
    elif symptom_type == "Hormonal_Imbalance":
        params.update({"query": "healthy fats"})
    elif symptom_type == "Menstrual_Issues":
        params.update({"query": "iron-rich"})
    elif symptom_type == "Skin_Hair_Problems":
        params.update({"query": "antioxidant"})

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        recipes = response.json().get('results', [])

        if len(recipes) < min_recipes:
            additional_params = {"apiKey": api_key, "query": "healthy meals", "number": min_recipes - len(recipes)}
            additional_response = requests.get(base_url, params=additional_params)
            additional_response.raise_for_status()
            recipes.extend(additional_response.json().get('results', []))

        return recipes[:min_recipes]

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching recipes for {symptom_type}: {e}")
        return []


# Function to predict symptoms for a new user
def predict_symptoms(user_data, model):
    user_df = pd.DataFrame([user_data])
    predictions = model.predict(user_df)

    symptom_names = ['Obesity', 'Insulin_Resistance', 'Hormonal_Imbalance',
                     'Menstrual_Issues', 'Skin_Hair_Problems', 'Ovulation_Problems']
    predicted_symptoms = dict(zip(symptom_names, predictions[0]))

    return predicted_symptoms


# Function to display recipes
def display_recipes_for_symptoms(predicted_symptoms):
    for symptom, is_present in predicted_symptoms.items():
        if is_present:
            st.subheader(f"Fetching recipes for: {symptom}")
            recipes = get_diet_recommendations(symptom)

            if recipes:
                for recipe in recipes:
                    title = recipe.get('title', 'Recipe Title Not Available')
                    st.write(f"- {title}")
            else:
                st.write(f"No recipes found for {symptom}")


# Streamlit App Layout
st.title("PCOS Diet Recommendation System")

# User Input Form
st.sidebar.header("Enter User Details")
bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
cycle_length = st.sidebar.number_input("Cycle length (days)", min_value=1, max_value=50, value=28)
fsh_lh = st.sidebar.number_input("FSH/LH Ratio", min_value=0.0, value=2.5)
tsh = st.sidebar.number_input("TSH (mIU/L)", min_value=0.0, value=3.0)
skin_darkening = st.sidebar.selectbox("Skin Darkening (Y/N)", [0, 1])
hair_loss = st.sidebar.selectbox("Hair Loss (Y/N)", [0, 1])
pimples = st.sidebar.selectbox("Pimples (Y/N)", [0, 1])
hair_growth = st.sidebar.selectbox("Hair Growth (Y/N)", [0, 1])
follicle_count = st.sidebar.number_input("Follicle No. (R)", min_value=0, max_value=20, value=10)

# Create user_data dictionary
user_data = {
    'BMI': bmi,
    'Cycle length(days)': cycle_length,
    'FSH/LH': fsh_lh,
    'TSH (mIU/L)': tsh,
    'Skin darkening (Y/N)': skin_darkening,
    'Hair loss(Y/N)': hair_loss,
    'Pimples(Y/N)': pimples,
    'hair growth(Y/N)': hair_growth,
    'Follicle No. (R)': follicle_count
}

if st.sidebar.button("Get Recommendations"):
    st.header("Predicted Symptoms")
    predicted_symptoms = predict_symptoms(user_data, rf_model)
    st.write(predicted_symptoms)

    st.header("Recipes Based on Symptoms")
    display_recipes_for_symptoms(predicted_symptoms)
