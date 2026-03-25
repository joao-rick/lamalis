import json
import os
from typing import Dict

import pika
from dotenv import load_dotenv
from pika.exceptions import AMQPConnectionError

from gen_routes import build_cripto_payload

load_dotenv()

class RabbitmqPublisher:
    def __init__(self) -> None:
        self.host = os.getenv('HOST', 'localhost')
        self.port = int(os.getenv('PORT', 5672))
        self.username = os.getenv('USERNAME', 'guest')
        self.password = os.getenv('PASSWORD', 'guest')
        self.exchange = os.getenv('EXCHANGE', '')
        self.routing_key = os.getenv('ROUTING_KEY', '')
        self.channel = self.__create_channel()
    
    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=pika.PlainCredentials(
                username=self.username,
                password=self.password
            )
        )

        try:
            channel = pika.BlockingConnection(connection_parameters).channel()
            if self.exchange:
                channel.exchange_declare(exchange=self.exchange, durable=True)
            else:
                channel.queue_declare(queue=self.routing_key, durable=True)
            return channel
        except AMQPConnectionError as exc:
            raise RuntimeError(
                f"Nao foi possivel conectar ao RabbitMQ em {self.host}:{self.port}. "
                "Verifique se o broker esta ligado e se HOST/PORT no .env estao corretos."
            ) from exc
    
    def send_message(self, body: Dict):
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )

    def close(self):
        if self.channel and self.channel.connection and self.channel.connection.is_open:
            self.channel.connection.close()


if __name__ == "__main__":
    payload = build_cripto_payload()
    rabbitmq_publisher = RabbitmqPublisher()
    rabbitmq_publisher.send_message(payload)
    rabbitmq_publisher.close()
    print("Mensagem enviada com sucesso:", payload)
