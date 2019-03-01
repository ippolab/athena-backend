FROM python:3.7


WORKDIR /app

ADD poetry.lock /app
ADD pyproject.toml /app

RUN pip install poetry && \
    poetry config settings.virtualenvs.create false && \
    poetry install --no-dev

COPY . /app

EXPOSE 8000

CMD python manage.py collectstatic --noinput && \
    python manage.py migrate && \
    gunicorn athena.wsgi -w 4 -b 0.0.0.0