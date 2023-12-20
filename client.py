# Example: reuse your existing OpenAI setup
import os
import openai

client = openai.OpenAI(
    base_url = "http://localhost:1234/v1",
    api_key = "hello there"
)

#openai.api_base = "http://localhost:1234/v1" # point to the local server
#openai.api_key = "" # no need for an API key

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Always answer in rhymes."},
        {"role": "user", "content": "Introduce yourself."}
    ],
)
print(completion.choices[0].message.content)
print(completion.choices[0].message)