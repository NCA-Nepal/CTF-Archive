FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1331

ENV FLASK_APP=app.py

CMD ["gunicorn", "--bind", "0.0.0.0:1331", "app:app"]

