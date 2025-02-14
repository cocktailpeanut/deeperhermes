from openai import OpenAI
import re
import gradio as gr
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
def detect(q):
    completion = client.chat.completions.create(
      model="deephermes-3-llama-3-8b-preview",
      messages=[
        {
          "role": "system",
          "content": f"you are an AI agent"
        },
        {
          "role": "user",
          "content": f"Does the following question require reasoning, or can a simple AI agent handle it? Say simple if simple AI agent can handle it. Say complex if requires reasoning: '{q}'. Only say 'simple' or 'complex' as an answer. Nothing else."
        }
      ],
      temperature=0.7,
    )
    return completion.choices[0].message.content

def query(q, system_prompt):
    response = client.chat.completions.create(
      model="deephermes-3-llama-3-8b-preview",
      messages=[
        {
          "role": "system",
          "content": system_prompt
        },
        {
          "role": "user",
          "content": q
        }
      ],
      stream=True,
      temperature=0.7,
    )
    str = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            str += chunk.choices[0].delta.content
            yield str

def ask(q, type):
    deep = "You are a deep thinking AI, you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering. You should start with a line '[THINKING]', and then print your thoughts and internal monologue first. And then print '[ANSWER]' and then print your solution or response to the problem."
    simple = "You are an AI agent."
    if re.search(r"simple", type, re.IGNORECASE):
        yield from query(q, simple)
    else:
        yield from query(q, deep)


def run(q, history):
    detected = detect(q)
    print(f"type = {detected}")
    yield from ask(q, detected)

demo = gr.ChatInterface(
    fn=run,
    type="messages"
)

demo.launch()
