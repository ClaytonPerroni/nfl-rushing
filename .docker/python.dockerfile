FROM python:3.9-slim AS builder
RUN apt-get update \
  && apt-get install -y --no-install-recommends
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 install --upgrade pip
WORKDIR /app/
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1