FROM python:3
RUN mkdir -p /app
WORKDIR /app
ADD app /app
WORKDIR /app

CMD [ "python", "./app.py" ]