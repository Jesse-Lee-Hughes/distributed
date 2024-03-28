from fastapi import FastAPI
import pika

app = FastAPI()


def send_message_to_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-service'))
    channel = connection.channel()
    channel.queue_declare(queue='jobs')
    channel.basic_publish(exchange='', routing_key='jobs', body='G\'Day World!')
    connection.close()


def check_queues():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-service'))
    channel = connection.channel()
    completed_jobs_info = channel.queue_declare(queue='completed_jobs', passive=True)
    jobs_info = channel.queue_declare(queue='jobs', passive=True)

    connection.close()

    return completed_jobs_info.method.message_count, jobs_info.method.message_count


@app.get("/")
def read_root():
    num_completed_jobs, num_jobs = check_queues()
    message = f"Total number of completed jobs: {num_completed_jobs}. Total number of jobs pending: {num_jobs}."

    send_message_to_rabbitmq()

    return {"message": message}