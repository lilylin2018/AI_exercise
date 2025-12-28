from openai import OpenAI
import os
api_key = os.environ['API_KEY']

client = OpenAI() #base_url api_key


def retrieval(query):
    return 

def generation(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message

