from openai import OpenAI
ashu_api = ""
client = OpenAI(api_key=ashu_key)

# older method 

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Write a fun fact about walmart!",
        }
    ],
    model="gpt-3.5-turbo",
    temperature=0.6,
    max_tokens=256,
    top_p=1,
    
)
print(response.choices[0].message.content)

## newer method

# calling LLM gpt model to interact with

response = client.responses.create(
    model="gpt-4o",
    top_p=1,
    input="Write a short bedtime story about a unicorn." # these days input is by default considering user ROLE 
)

print(response.output_text)