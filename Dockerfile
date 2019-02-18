FROM python:3.7

EXPOSE 8000

WORKDIR /app

ADD poetry.lock /app
ADD pyproject.toml /app

RUN pip install poetry && \
    poetry config settings.virtualenvs.create false && \
    poetry install

COPY . /app

CMD python manage.py migrate && \
    gunicorn athena.wsgi -w 4 -b 0.0.0.0