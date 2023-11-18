from llama_cpp import Llama

# Put the location of to the GGUF model that you've download from HuggingFace here
model_path = "/Users/shubhamkumar/Desktop/GenContentHub/llama/llama-2-7b-chat.Q2_K.gguf"

# Create a llama model
model = Llama(model_path=model_path)

# Prompt creation
system_message = "You are a helpful assistant"
user_message = "Generate 5 slogan using shoe great fit durable"

prompt = f"""<s>[INST] <<SYS>>
{system_message}
<</SYS>>
{user_message} [/INST]"""

# Model parameters
max_tokens = 100

# Run the model
output = model(prompt, max_tokens=max_tokens, echo=True)

# Print the model output
print(output)
