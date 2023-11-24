FROM python:3.11

COPY koroche /koroche/
COPY requirements.txt /koroche/requirements.txt
COPY configs/config.yml /configs/config.yml

WORKDIR /koroche

RUN pip install -r requirements.txt

ENV PYTHONPATH=/

CMD [ "python", "app.py" ]