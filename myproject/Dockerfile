FROM python:3.10

RUN curl -sSL https://install.python-poetry.org | python -

WORKDIR /app

ENV PATH="/root/.local/bin:$PATH"

COPY poetry.lock pyproject.toml /app/
RUN pip install poetry

COPY . /app/

CMD ["python", "manage.py", "runserver",  "0.0.0.0:8000"]
