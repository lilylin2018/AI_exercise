from openai import OpenAI
import os
api_key = os.environ['API_KEY']

client = OpenAI() #base_url api_key


def retrieval(query):
    context = ""
    #向量搜索
    #query相關文件添加到context

    return context 

def augmented(query, context=""):
    if not context:
        return f"請回答以下問題: {query}"
    else:
        prompt = f"""請根據上下文訊息來回答問題，如果上下文訊息不足以回答問題，請直接說:"根據提供的上下文訊息，無法回答"
        上下文:
        {context}

        問題:{query}"""

        return prompt

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


if __name__ == '__main__':
    query = "who are you?"

    context = retrieval(query)
    prompt = augmented(query, context)
    resp = generation(prompt)
    
    print(resp)