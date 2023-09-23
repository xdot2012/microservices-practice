from contextlib import asynccontextmanager
from functools import lru_cache
from fastapi import FastAPI
import pika

app = FastAPI()

def get_connection():
    return pika.BlockingConnection(pika.ConnectionParameters('localhost'))

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


connection = get_connection()
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello',
                auto_ack=True,
                on_message_callback=callback)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    connection.close()


@app.get("/")
async def root():
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
    return {"message": "Hello World"}
