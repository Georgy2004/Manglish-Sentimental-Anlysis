
import streamlit as st
import joblib

# Load the trained model
model = joblib.load('manglish_model.pkl')

# Page configuration
st.set_page_config(
    page_title="Manglish Sentiment Analyzer",
    page_icon="💬",
    layout="centered"
)

# Application title
st.title("💬 Manglish Sentiment Analyzer")

st.write(
    "Enter a Manglish sentence to predict its sentiment."
)

# User input
user_input = st.text_area(
    "Enter your Manglish text:",
    placeholder="Example: Ee movie adipoli aanu!"
)

# Prediction button
if st.button("Predict Sentiment"):

    if user_input.strip():

        # Make prediction
        prediction = model.predict([user_input])[0]

        # Display result
        st.subheader("Prediction Result")

        sentiment = str(prediction).lower()

        if sentiment == "positive":
            st.success(f"😊 Positive Sentiment: {prediction}")

        elif sentiment == "negative":
            st.error(f"😞 Negative Sentiment: {prediction}")

        elif sentiment == "neutral":
            st.info(f"😐 Neutral Sentiment: {prediction}")

        else:
            st.write(f"Predicted class: {prediction}")

    else:
        st.warning("Please enter some text!")
