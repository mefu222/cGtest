import openai

#plz change your api_key
openai.api_key = "sk-***"

response = openai.ChatCmpletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": "Nyokkeyとは"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)
