# Deeper Hermes

Deephermes is really cool because a single model can act either as a normal agent, or a deep thinking AI simply by using system prompts.

**What if you don't even need a system prompt, and the model automatically acts based on its OWN judgement?**

![deeperhermes.gif](deeperhermes.gif)

In above example:

1. The first question is a simple question, so the model acts as a basic agent
2. The second question is also simple, so it acts as a simple agent
3. The third question is a bit complex and requires resasoning, so it starts with `[THINKING]` and then ends with `[ANSWER]`, confirming that it's using the deep thinking mode.

# How it works

1. Deeper Hermes is made up of 2 separate queries.
2. The first one is to ask which mode to use (normal agent vs. deep thinking AI)
3. The answer from 2 decides the system prompt that gets fed into the actual question.

# Get started

## A. 1-click Launch

1. First install [LM Studio](https://lmstudio.ai/)
2. Install Deeper Hermes on pinokio.computer with 1 click.

## B. Manual Install

First install [LM Studio](https://lmstudio.ai/)

Then load nousresearch_deephermes-3-llama-3-8b-preview into LMStudio:

```
lms load nousresearch_deephermes-3-llama-3-8b-preview -y
```

Once the LMStudio server is running and has loaded the model, activate virtual environment

```
source env/bin/activate (mac/linux)
.\env\Scripts\activate (windows)
```

Next, install dependencies:

```
pip install -r requirements.txt
```

Then run with:

```
python app.py
```
