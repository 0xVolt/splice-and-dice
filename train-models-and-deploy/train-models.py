# Import necessary libraries
from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Load XSum dataset
dataset = load_dataset('xsum', split='train[:10]')

# Define the models and tokenizer
model1 = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer1 = T5Tokenizer.from_pretrained('t5-base')

model2 = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer2 = T5Tokenizer.from_pretrained('t5-small')

model3 = T5ForConditionalGeneration.from_pretrained('t5-large')
tokenizer3 = T5Tokenizer.from_pretrained('t5-large')

# Define the training arguments
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy = "epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=1,
    weight_decay=0.01,
    push_to_hub=False,
    logging_dir='./logs',
    logging_steps=10,
    load_best_model_at_end=True,
    metric_for_best_model='rouge2',
    greater_is_better=True
)

# Define the trainer objects
trainer1 = Trainer(
    model=model1,
    args=training_args,
    train_dataset=dataset,
    data_collator=lambda data: {'input_ids': tokenizer1(data['document'], truncation=True, padding='max_length')['input_ids'], 
                                'attention_mask': tokenizer1(data['document'], truncation=True, padding='max_length')['attention_mask'], 
                                'labels': tokenizer1(data['summary'], truncation=True, padding='max_length')['input_ids']}
)

trainer2 = Trainer(
    model=model2,
    args=training_args,
    train_dataset=dataset,
    data_collator=lambda data: {'input_ids': tokenizer2(data['document'], truncation=True, padding='max_length')['input_ids'], 
                                'attention_mask': tokenizer2(data['document'], truncation=True, padding='max_length')['attention_mask'], 
                                'labels': tokenizer2(data['summary'], truncation=True, padding='max_length')['input_ids']}
)

trainer3 = Trainer(
    model=model3,
    args=training_args,
    train_dataset=dataset,
    data_collator=lambda data: {'input_ids': tokenizer3(data['document'], truncation=True, padding='max_length')['input_ids'], 
                                'attention_mask': tokenizer3(data['document'], truncation=True, padding='max_length')['attention_mask'], 
                                'labels': tokenizer3(data['summary'], truncation=True, padding='max_length')['input_ids']}
)

# Train the models
trainer1.train()
trainer2.train()
trainer3.train()
