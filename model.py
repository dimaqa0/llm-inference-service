from transformers import AutoTokenizer, AutoModelForCausalLM
import time

model_name = "sshleifer/tiny-gpt2"  # Very small model for CPU

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_text(prompt: str):
    start = time.time()

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=40)
    text = tokenizer.decode(outputs[0])

    latency = time.time() - start
    return text, latency

