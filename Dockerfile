FROM python:3.11

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /opt

RUN groupadd -r starlette && useradd -r -s /bin/false -g starlette starlette
COPY --chown=starlette:starlette ./app /opt/app
USER starlette
