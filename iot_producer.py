from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    sensor_data = {
        'temperature': round(random.uniform(20, 40), 2),
        'humidity': round(random.uniform(30, 70), 2)
    }
    print("Sending data:", sensor_data)
    producer.send('iot-topic', value=sensor_data)
    time.sleep(2)