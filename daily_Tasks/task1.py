
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "I love artificial intelligence",
    "AI is fascinating",
    "Bananas are yellow"
]

embeddings = model.encode(sentences)

print(embeddings.shape)
print(embeddings[0,1])