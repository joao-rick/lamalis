import pika

connection = pika.BlockingConnection()
channel = connection.channel()

for method_frame, properties, body in channel.consume('test'):
    print(method_frame, properties, body)
    channel.basic_ack(method_frame.delivery_tag)

    if method_frame.delivery_tag == 10:
        break

requeued_messages = channel.cancel()
print('Requeued %i messages' % requeued_messages)
connection.close()