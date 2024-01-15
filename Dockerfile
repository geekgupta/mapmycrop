FROM python:3.10-slim-buster

# Install necessary packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    curl \
    git \
    gnupg \
    gcc \
    libffi-dev \
    libssl-dev \
    libldap2-dev \
    libsasl2-dev \
    postgresql-client \
    imagemagick \
    sudo && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /backend
COPY requirements.txt /backend/

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install tzdata

RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install -r requirements.txt && pip install tzdata
COPY . /backend/

EXPOSE 8000
