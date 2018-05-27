FROM python:2.7-slim

ENV DOCKER="YES" \
    HOME=/app \
    RASA_PYTHON_PACKAGES=/usr/local/lib/python2.7/dist-packages

WORKDIR ${HOME}

COPY . ${HOME}

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends build-essential git-core openssl libssl-dev libffi6 libffi-dev curl  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install spacy

VOLUME /vector

CMD python load_fastText.py