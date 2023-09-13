# Learning llms and genai for Dev,Sec,Ops
## What is this repo about ?
This repo aims to structure various information about LLMs and GenAi in a **lesson narrative** that is easily understood by traditional software engineering. It highlights the aspects you need to understand from development, operations and security perspective. While there is a lot of material out there, I found myself explaining the same things over and over again and developed a narrative.

The lessons are mainly based on the [Langchain](https://github.com/langchain-ai/langchain) framework and expects a bit of familiarity with the Python programming language. Many examples have been borrowed from pages and attribution is given where possible.

## History of this repo
- The initial lessons structure was formed during a [GenAI hackaton](https://www.linkedin.com/feed/update/urn:li:activity:7101235295735488512/) graceously hosted by [Techstrong/MediaOps](https://techstronggroup.com/)
- The lessons were refined for a presentation at the [London Devops Meetup group](https://www.meetup.com/london-devops/events/294948985/?utm_medium=referral&utm_campaign=share-btn_savedevents_share_modal).
- Others are making plans to run their own version of it

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
