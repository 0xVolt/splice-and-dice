import torch
from transformers import T5Config, T5ForConditionalGeneration

# Set the path to the checkpoints file
checkpoint_path = "/home/volt/code/splice-and-dice/assets/weights/fine-tuned-t5-weights.pt"

# Load the weights from the checkpoints file
state_dict = torch.load(checkpoint_path, map_location=torch.device('cpu'))

# Set the T5 configuration to the T5-base model
config = T5Config.from_pretrained("t5-base")

# Create a T5 model with the same configuration as the T5-base model
model = T5ForConditionalGeneration(config=config)

# Load the weights into the T5 model
model.load_state_dict(state_dict)

# Save the model in the Transformers format
model.save_pretrained("../assets/weights/")
