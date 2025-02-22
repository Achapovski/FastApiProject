FROM python:3.12.0
LABEL authors="HP"

ENV HOME=/home/FastAPI \
    APP_HOME=/home/FastAPI/app \
    PYTHONPATH="$PYTHONPATH:/home/FastAPI"
#    PYTHONPATH=/home/fast

RUN mkdir -p $APP_HOME && groupadd -r fastgroup && useradd -r -g fastgroup fast

WORKDIR $HOME

COPY app app
COPY alembic.ini .
COPY requirements.txt app

RUN pip install --upgrade pip && pip install -r app/requirements.txt

USER fast
