FROM python:3.9.13-slim AS runtime

COPY gerador /app/gerador

WORKDIR /app/gerador

RUN pip install --no-cache-dir -r gerador/requirements.txt

CMD ["python", "gerador/publisher.py"]

#docker build -t gerarador:1.0 /gerador
#docker run gerarador:1.0