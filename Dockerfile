FROM python:3.10 AS metadata
LABEL maintainer="Stefano Pigozzi <me@steffo.eu>"
LABEL description="A Telegram bot to delete messages sent outside of threads"

FROM metadata AS workdir
WORKDIR /usr/src/threadkiller

FROM workdir AS poetry
RUN pip install "poetry"

FROM poetry AS dependencies
COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock
RUN poetry install --no-root --no-dev

FROM dependencies AS package
COPY . .
RUN poetry install

FROM package AS environment
ENV PYTHONUNBUFFERED=1

FROM environment AS entrypoint
ENTRYPOINT ["poetry", "run", "python", "-m"]
CMD ["threadkiller"]
