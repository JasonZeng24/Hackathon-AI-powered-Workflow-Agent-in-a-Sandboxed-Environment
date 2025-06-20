FROM python:3.11-slim
WORKDIR /sandbox
RUN apt update && apt install -y bash git