from typing import Dict
import pika
import json
from dotenv import load_dotenv
import os
from gen_routes import generate_cripto

load_dotenv()

class RabbitmqPublisher:
    def __init__(self) -> None:
        self.host = os.getenv('HOST')
        self.port = int(os.getenv('PORT'))
        self.username = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')
        self.exchange = os.getenv('EXCHANGE')
        self.routing_key = os.getenv('ROUTING_KEY')
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

        return pika.BlockingConnection(connection_parameters).channel()
    
    def send_message(self, body: Dict):
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )

rabbitmq_publisher = RabbitmqPublisher()
rabbitmq_publisher.send_message(generate_cripto())