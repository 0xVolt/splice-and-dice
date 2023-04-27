import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

# Define a function to generate predictions
def predict(text):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits.detach().cpu().numpy()
    return logits[0]

# Create the Streamlit application
def main():
    st.title("Hugging Face Transformer Example")
    text = st.text_input("Enter some text:")
    if text:
        logits = predict(text)
        st.write("Prediction:", logits)

if __name__ == "__main__":
    main()
