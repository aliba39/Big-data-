# 🛰️ IoT Sensor Simulation with Apache Kafka (Python)

This project simulates IoT sensors (like temperature and humidity) and sends the data to an Apache Kafka topic using Python. It also includes a Kafka consumer script to read and print the sensor data in real time.

---

## 📦 Requirements

- Apache Kafka (installed and running)
- Python 3.7+
- `kafka-python` library

Install dependencies using:

```bash
pip install kafka-python
```

---

## ⚙️ Kafka Setup (Windows)

1. Download Kafka binary (not source) from: https://kafka.apache.org/downloads
2. Extract it to `C:\kafka`
3. Start Zookeeper:

```bash
cd C:\kafka
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
```

4. Start Kafka server (in a new terminal):

```bash
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

5. Create Kafka topic:

```bash
.\bin\windows\kafka-topics.bat --create --topic iot-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

---

## 🧪 Simulated Sensor Data

### Producer (`iot_producer.py`)

This script simulates temperature and humidity readings and sends them to the Kafka topic `iot-topic` every 2 seconds.

```python
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
```

---

### Consumer (`iot_consumer.py`)

This script reads the data from `iot-topic` and prints it to the terminal.

```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'iot-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    print("Received:", message.value)
```

---

## ▶️ How to Run

1. Start Kafka and Zookeeper (see setup above).
2. In one terminal, run the **consumer**:

```bash
python iot_consumer.py
```

3. In another terminal, run the **producer**:

```bash
python iot_producer.py
```

You should see messages being sent and received, like:

**Producer Output:**
![image](https://github.com/user-attachments/assets/0ea2c47c-2a9c-4ab8-bdfe-4aa619b43ff3)


**Consumer Output:**
![image](https://github.com/user-attachments/assets/605ad053-d6c0-4e5f-b82a-8afd43fc1033)


---

## 📈 Future Ideas

- Connect a real ESP32 sensor and send data to this producer
- Store data in a database (MongoDB, PostgreSQL)
- Visualize live data with Flask and Chart.js
- Deploy with Docker and Kafka UI

---

## 🧑‍💻 Author

Ahmad Ayoub – [GitHub](https://github.com/yourusername)

---

## 📄 License

MIT License
