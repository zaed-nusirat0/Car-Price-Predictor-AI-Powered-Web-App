FROM python:latest

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "8000"]

