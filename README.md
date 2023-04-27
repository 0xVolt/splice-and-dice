# Semester VI Minor Project

## Objective of the Project 
Modularizing Multi-Source Text Summarization with Transformer-based Deep Learning and NLP techniques in a Full-Stack Web Application.

Text summarizer that has two modes: one to input a blob of text and another to input documents. It figures out what model to use for summarization in the backend through evaluation of their respective outputs and displays the optimal summary to the user. 

## TODO
- Working with models
  - Import models
  - Fine-tune them
  - Evaluate them on validation and testing sets
- Create Streamlit application
  - Inputs
    - Keywords
      - Speech recognition
      - Text input
        - Take notes from the NES tagging video
    - Tab for text
    - Another for PDFs
    - Both together if possible
  - Drop-down to select models
    - Rank them on evaluation metric
  - Output
    - Click to copy function
- Presentation for implementation
  - Comparative analysis for models
    - 
    - Validation loss for each model
- Import pre-trained transformers for abstractive text summarization given inputs either through keywords or speech
- Create text summarizer streamlit app
- Code the 
- Speech recognition system for keywords
- Connect to database
- Login System?

## Models we're using
T5: This model is a transformer-based model that has achieved state-of-the-art results on several NLP tasks, including text summarization. It can be fine-tuned on the XSum dataset for summarizing research papers.

BART: BART is another transformer-based model that can be used for abstractive text summarization. It has achieved state-of-the-art results on several benchmark datasets and can be fine-tuned on the CNN/Daily Mail dataset for summarizing research papers.

GPT-2: GPT-2 is a large-scale transformer-based language model that has been pre-trained on a diverse range of text data. It can be fine-tuned on the CNNDM dataset for summarizing research papers.

Pegasus: Pegasus is a sequence-to-sequence transformer-based model that has been specifically designed for abstractive text summarization. It has achieved state-of-the-art results on several benchmark datasets and can be fine-tuned on the XSum dataset for summarizing research papers.

ProphetNet: ProphetNet is another transformer-based model that has been specifically designed for sequence-to-sequence tasks. It has achieved state-of-the-art results on several benchmark datasets and can be fine-tuned on the XSum dataset for summarizing research papers.

## Stuff to talk about
- Using a `requirements.txt` to manage dependencies in Python

## References
- [`txtai`s Official GitHub Repository](https://github.com/neuml/txtai)
- [`PyPDF2`s Official GitHub Repository](https://github.com/py-pdf/pypdf)