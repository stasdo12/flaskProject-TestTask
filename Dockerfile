FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc python3-dev


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

ENV FLASK_APP=app.py
ENV FLASK_ENV=production


