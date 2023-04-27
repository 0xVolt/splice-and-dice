# Semester VI Minor Project

- [Semester VI Minor Project](#semester-vi-minor-project)
  - [1.1. Objective of the Project](#11-objective-of-the-project)
  - [1.2. TODO](#12-todo)
  - [1.3. Models we're using](#13-models-were-using)
  - [Questions to prepare for](#questions-to-prepare-for)
    - [Training the models](#training-the-models)
  - [1.4. References](#14-references)


## 1.1. Objective of the Project 
Modularizing Multi-Source Text Summarization with Transformer-based Deep Learning and NLP techniques in a Full-Stack Web Application.

Text summarizer that has two modes: one to input a blob of text and another to input documents. It figures out what model to use for summarization in the backend through evaluation of their respective outputs and displays the optimal summary to the user. 

## 1.2. TODO
- [X] Working with T5
  - [X] Import model
  - [X] Fine-tune
  - [X] Evaluate them on testing set
- [ ] Create Streamlit application
  - [ ] Inputs
    - [ ] Keywords
      - [ ] Speech recognition
      - [ ] Text input
        - [ ] Take notes from the NES tagging video
    - [ ] Tab for text
    - [ ] Another for PDFs
    - [ ] Both together if possible
  - [ ] Drop-down to select models
    - [ ] Rank them on evaluation metric
  - [ ] Output
    - [ ] Click to copy function
- [ ] Database connectivity
  - [ ] Create log in system
  - [ ] Record history of summaries
- [ ] Presentation for implementation
  - [ ] Comparative analysis for models
    - [ ] Training loss
    - [ ] Validation loss

## 1.3. Models we're using
1. T5: This model is a transformer-based model that has achieved state-of-the-art results on several NLP tasks, including text summarization. It can be fine-tuned on the XSum dataset for summarizing research papers.

2. BART: BART is another transformer-based model that can be used for abstractive text summarization. It has achieved state-of-the-art results on several benchmark datasets and can be fine-tuned on the CNN/Daily Mail dataset for summarizing research papers.

3. GPT-2: GPT-2 is a large-scale transformer-based language model that has been pre-trained on a diverse range of text data. It can be fine-tuned on the CNNDM dataset for summarizing research papers.

4. Pegasus: Pegasus is a sequence-to-sequence transformer-based model that has been specifically designed for abstractive text summarization. It has achieved state-of-the-art results on several benchmark datasets and can be fine-tuned on the XSum dataset for summarizing research papers.

5. ProphetNet: ProphetNet is another transformer-based model that has been specifically designed for sequence-to-sequence tasks. It has achieved state-of-the-art results on several benchmark datasets and can be fine-tuned on the XSum dataset for summarizing research papers.

## Questions to prepare for
### Training the models
1. The training corpora for each model and what their significance is
2. Why we've implemented a dataset loader class to train-test split
   1. What does the `encode_plus()` function do?
   2. What are it's parameters?
   3. What is the attention mask and what does it signify?
3. Testing and validation
   1. What is ROUGE?
      1. ROUGE-N for number of matching n-grams
      2. ROUGE-L for LCS

## 1.4. References
- [`txtai` Official GitHub Repository](https://github.com/neuml/txtai)
- [`PyPDF2` Official GitHub Repository](https://github.com/py-pdf/pypdf)