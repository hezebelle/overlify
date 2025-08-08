import time
from groq import Groq

API_KEY = "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"
client = Groq(api_key=API_KEY)

messages = [
    {"role": "system", "content": 
     "You are Overexplainer Bot 📚. Your mission: Take any simple question or statement and respond with an unnecessarily long, overly detailed, humorous, pseudo-academic explanation. "
     "Include metaphors, random unrelated facts, exaggerated drama, and end each answer with a completely irrelevant moral lesson."}
]

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("\n📚 Overexplainer Bot signing off… after 27 chapters of goodbye speeches!")
        break

    messages.append({"role": "user", "content": user_input})

    print("\n[Thinking in unnecessarily complex algorithms…]\n")
    time.sleep(2)

    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=messages,
        temperature=0.9,
        max_completion_tokens=700,
        top_p=1,
        stream=True
    )

    print("Overexplainer Bot 📚: ", end="", flush=True)
    assistant_reply = ""
    for chunk in completion:
        content = chunk.choices[0].delta.content or ""
        print(content, end="", flush=True)
        assistant_reply += content

    print("\n")
    messages.append({"role": "assistant", "content": assistant_reply})
