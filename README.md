# Learning llms and genai for Dev,Sec,Ops
## What is this repo about ?
This repo aims to structure various information about LLMs and GenAi in a **lesson narrative** that is easily understood by traditional software engineering. It highlights the aspects you need to understand from development, operations and security perspective. While there is a lot of material out there, I found myself explaining the same things over and over again and developed a narrative.

The lessons are mainly based on the [Langchain](https://github.com/langchain-ai/langchain) framework and expects a bit of familiarity with the Python programming language. Many examples have been borrowed from documentation pages and attribution is given where possible. Kudos to Langchain for collection so much material !

## Lessons overview
### Developer
- Calling a simple LLM using OpenAI
- Looking at debugging in Langchain
- Chatting with OpenAI as model
- Using prompt templates
- Use of Docloader to read your local files and prepare them for the LLM
- Explain the calculation and use of embeddings
- Understand how splitting and chunking is important
- Loading embeddings and documents in a vector database
- Use a chain for Questions and Answers to implement the RAG pattern (Retrieval Augmented Generation)
- Show the use of OpenAI documentation to have the llm generate calls to find realtime information
- Implement an Agent and provide it with tools to get more realtime information

## Operations
- Find out how much tokens you are using and the cost
- How to cache your calls to an LLM using exact matching or embeddings
- How to cache the calculation of embeddings and run the calculation locally
- Run your own local LLM (using Ollama)
- Track your calls and log them to a file (using a callback handler)
- Impose output structure (as JSON) and have the LLM retry if it's not correct

## Security
- Explain the OWASP top 10 for LLMS
- Show how simple prompt injection works and some mitigation strategies
- How to detect prompt injection using a 3rd party model from Hugginface
- Detect project injection by using a prompt
- Check the answer llms provide and reflect if it ok
- Use a huggingface model to detect if an LLM output was toxic
- Show a simple prompt for asking the llm's opinon on Kubernetes and Trivy vulnerabilities

Jump right in <https://github.com/jedi4ever/learning-llms-and-genai-for-dev-sec-ops/tree/main/lessons>
More to come !

## History of this repo
- The initial lessons structure was formed during a [GenAI hackaton](https://www.linkedin.com/feed/update/urn:li:activity:7101235295735488512/) graceously hosted by [Techstrong/MediaOps](https://techstronggroup.com/)
- The lessons were refined for a presentation at the [London Devops Meetup group](https://www.meetup.com/london-devops/events/294948985/?utm_medium=referral&utm_campaign=share-btn_savedevents_share_modal).
- [Others are making plans](https://x.com/devopsdaysATL/status/1699833229795291609?) to run their own version of it

## How can you help ?
- Let us know what topic you'd like to see a lesson on ? Open a github issue to ask it
- Submit new lessons, send us corrections etc.. to improve it.

- Run your own meetup/hackaton using this repo as base and report back ! We love to hear those stories

## Requirements to run this repo (needs more love)

### Run it using a devcontainer
This project contains a devcontainer to run the repo locally.
Or you can use Google collab or so to run the notebooks

### Run it locally
- We used Microsoft VSCode to run the demo
- We run the python & jupyter notebooks locally
- We use poetry as our virtual env python manager

Poetry is the new package manager on the block. Similar to Conda or Pip with venv.

```shell
poetry init
poetry install
```

### configure vscode to use poetry
- find the poetry env path `poetry env info --path`
- in vscode `view -> command pallete -> select interpreter path -> enter interpreter path`
- add the path `/Users/patrick.debois/Library/Caches/pypoetry/virtualenvs/london-devops-VW7lFx7f-py3.11` + add `/bin/python to it`

### configure jupyter notebooks
- install vscode plugin
- install ipykernel
