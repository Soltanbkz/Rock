import openai

openai.api_key = "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"

def answer_question(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response["choices"][0]["text"].strip()
    return answer

while True:
    user_input = input("You: ")
    answer = answer_question(user_input)
    print("AI: " + answer)
