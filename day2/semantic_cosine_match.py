# importing module 
from openai import OpenAI
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

# loading .env file 
load_dotenv() # auto load .env file 

client = OpenAI()

# Step 2: Function to get embeddings (updated for v1.0+)
def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    response = client.embeddings.create(
        input=[text],
        model=model
    )
    return np.array(response.data[0].embedding)

# take text examples to do embedding 
# Step 3: Example texts
text1 = "I love programming in Python."
text2 = "Python coding is my passion."
text3 = "I enjoy playing football."

# do embedding of above texts

embedding1 = get_embedding(text1)
embedding2 = get_embedding(text2)
embedding3 = get_embedding(text3)

# using cosine distance find similarty (-1,0,+1)-- more higher --> more similar
# using cosine_similarity module
similarity1 = cosine_similarity([embedding1], [embedding2])
similarity2 = cosine_similarity([embedding1], [embedding3])
similarity3 = cosine_similarity([embedding2], [embedding3])

#priting similarty
print("Similarity between text1 and text2:", similarity1[0][0])
print("Similarity between text1 and text3:", similarity2[0][0])
print("Similarity between text2 and text3:", similarity3[0][0])

## note that similarity values are between 0 and 1, where 1 means identical
# and 0 means no similarity.
# You can interpret these values to understand how similar the texts are to each other.
# For example, a value of 0.8 indicates a high degree of similarity,
# while a value of 0.2 indicates low similarity.
