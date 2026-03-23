FROM python:3.9.13

COPY . /app/

WORKDIR /app/

RUN pip install -r requirements.txt

CMD ["python", "publisher.py"]

#docker build -t gerador:1.0 /gerador
#docker run gerador:1.0