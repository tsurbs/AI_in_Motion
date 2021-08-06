from transformers import pipeline
  
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

result = generator("EleutherAI has", do_sample=True, min_length=50)

print(result)

