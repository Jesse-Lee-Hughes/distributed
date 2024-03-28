import pika
import time
import random


connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-service'))
channel = connection.channel()
channel.queue_declare(queue='jobs')
channel.queue_declare(queue='completed_jobs')


def callback(ch, method, properties, body):
    sleep_time = random.uniform(1, 10)
    time.sleep(sleep_time)
    channel.basic_publish(
        exchange='',
        routing_key='completed_jobs',
        body=f'Job completed after {sleep_time} seconds.',
    )


channel.basic_consume(
    queue='jobs',
    on_message_callback=callback,
    auto_ack=True,
)

channel.start_consuming()