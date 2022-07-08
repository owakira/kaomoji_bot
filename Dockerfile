FROM python:3.10-slim-bullseye

WORKDIR /bot

RUN python -m venv venv
COPY . /bot/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
CMD ["python", "-m", "src"]