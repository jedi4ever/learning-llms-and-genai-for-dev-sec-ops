# LLMs & Langchain explained for Dev, Sec, Ops

** Note: cleanup in progress **

## Requirements to run this repo

- We use VSCode to demo
- We run the python & jupyter notebooks locally
- We use poetry as a our virtual env python manager

### install poetry 
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
