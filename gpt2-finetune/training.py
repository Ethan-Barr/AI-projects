import json
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling, TrainingArguments, Trainer

raw_data = 'data_tolokers.json'

with open(raw_data, 'r') as f:
    df = json.load(f)

data  = []

for x in df:
    for y in range(len(x['dialog'])-1):
        a = '[BOT] : ' + x['dialog'][y+1]['text']
        q = '[YOU] : ' + x['dialog'][y]['text']
        data.append(q)
        data.append(a)

file_path = 'chatbot.txt'

with open(file_path, 'w') as f:
        for line in data:
                f.write(line + '\n')




# Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Load and tokenize your fine-tuning dataset
train_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="chatbot.txt",  # Replace with the path to your dataset
    block_size=128  # Adjust as needed
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./fine-tuned-gpt2",
    overwrite_output_dir=True,
    num_train_epochs=3,  # Adjust as needed
    per_device_train_batch_size=8,  # Adjust as needed
    save_steps=10_000,
    save_total_limit=2,
)



# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained("fine-tuned-gpt2")
