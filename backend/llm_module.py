from transformers import pipeline

llm = pipeline("text-generation", model="gpt2")

def generate(prompt):
    result = llm(prompt, max_length=80)
    return result[0]["generated_text"]
