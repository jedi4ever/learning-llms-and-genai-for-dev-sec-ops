FROM python:3.11.2-bullseye

# install bash completion - to make make work
RUN apt-get update && apt-get install -y bash-completion

# Add user python - this also creates the homedir
RUN useradd -ms /bin/bash python

# Create some dirs 
# used for poetry env
RUN mkdir -p /opt/poetry
RUN mkdir -p /opt/poetry-cache
# used for poetry virtual envs
RUN mkdir -p /opt/virtual-envs

# set the correct ownership
RUN chown python /opt/virtual-envs
RUN chown python /opt/poetry
RUN chown python /opt/poetry-cache

# Switch to python user
USER python


# Create a Python virtual environment for Poetry and install it
# Define the version of Poetry to install (default is 1.5.1)

ARG POETRY_VERSION=1.5.1
ARG POETRY_HOME=/opt/poetry

RUN python3 -m venv ${POETRY_HOME} && \
    $POETRY_HOME/bin/pip install --upgrade pip && \
    $POETRY_HOME/bin/pip install poetry==${POETRY_VERSION}

# Test if Poetry is installed in the expected path
RUN echo "Poetry version:" && $POETRY_HOME/bin/poetry --version

# add poetry to paths
RUN echo $PATH
RUN echo "export PATH=$PATH:/opt/poetry/bin" >> ~/.bashrc
RUN cat ~/.bashrc
RUN echo $PATH

COPY poetry.lock pyproject.toml ./
RUN $POETRY_HOME/bin/poetry install --no-root