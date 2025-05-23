FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--reload",]
CMD python3 manage.py runserver 0.0.0.0:8000
