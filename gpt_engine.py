import openai

openai.api_key = "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"

async def generate_reply(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
