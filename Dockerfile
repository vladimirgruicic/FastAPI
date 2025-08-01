FROM python:3.8

WORKDIR /app

COPY . . 

RUN apt update && apt upgrade -y

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ] command