FROM python:3.11.6-slim-bookworm

# Declare environment variables
ENV \
    # Python
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app:$PYTHONPATH \
    \
    # Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # Poetry
    POETRY_VERSION=1.7.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH=/venv/.venv/bin:$PATH \
    \
    # Taskfile
    TASK_VERSION=3.12.1 \
    \
    # Locales
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

# Update system dependencies
RUN \
    set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        locales \
        gettext \
        gosu \
        wget \
        libpq-dev \
    && rm -rf /var/cache/apt/* /var/lib/apt/lists/* 

# Configure locales
RUN \
    set -ex \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen

# Install Taskfile
RUN \
    set -ex \
    && wget --progress=dot:giga https://github.com/go-task/task/releases/download/v${TASK_VERSION}/task_linux_amd64.tar.gz \
    && tar -C /usr/local/bin -xzvf task_linux_amd64.tar.gz \
    && rm task_linux_amd64.tar.gz \
    && chown root:root /usr/local/bin/task

# Install project dependencies with Poetry
WORKDIR /venv
COPY Taskfile.yml poetry.lock pyproject.toml ./
RUN \
    set -ex \
    && pip install -U pip setuptools \
    && pip install poetry==${POETRY_VERSION} \
    && task deploy:build

# Create a non-root user
RUN addgroup --gid 10001 user && adduser --uid 10000 --gid 10001 user

# Copy project into user folder
WORKDIR /app
COPY . /app

# The result of this Dockerfile is an /app folder that mirrors this Dockerfile's directory.
# All code and dependencies are root-owned, but the task starts as user.
USER user
EXPOSE 8000
ENTRYPOINT ["task"]
CMD ["deploy:run"]
