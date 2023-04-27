import streamlit as st
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load tokenizer and model
tokenizer = T5Tokenizer.from_pretrained('t5-base')
model = T5ForConditionalGeneration.from_pretrained('t5-base')

# Set device to GPU if available, otherwise use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# Define function for generating summaries
def generate_summary(text):
    # Tokenize input text
    input_ids = tokenizer.encode(text, return_tensors='pt').to(device)

    # Generate summary
    summary_ids = model.generate(input_ids=input_ids,
                                 num_beams=4,
                                 no_repeat_ngram_size=2,
                                 min_length=30,
                                 max_length=100,
                                 early_stopping=True)
    
    # Decode summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

# Set up Streamlit app
st.title('Text Summarizer')

text_input = st.text_area('Enter text to summarize:')
if st.button('Summarize'):
    summary = generate_summary(text_input)
    st.write('Summary:', summary)
