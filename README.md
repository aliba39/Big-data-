# 🧪 TP Apache Kafka – Windows + IoT Simulation

This repository contains a complete practical lab (TP) on **Apache Kafka**, including installation, topic creation, producer-consumer demo, multiple broker configuration, and an IoT simulation project using Python.

---

## 📋 Table of Contents

1. [Apache Kafka Installation under Windows](#Apache-Kafka-Installation-under-Windows)
2. [Creation of a topic](#creation-of-a-topic)
3. [Example consumer producer](#Example-producer-Consumer)
4. [Configuration of several brokers](#Configuration-of-several-brokers)
5. [IoT + Kafka project](#IoT-Kafka-project)

---

## 1️⃣ Apache Kafka installation under windows

### ✅ Prerequis

- Java JDK 8 or more (`java -version`)
- Python 3.7+ (for the IoT project)

### 📥 Étapes

1. Download the ** Binary ** version of Kafka: https://kafka.apache.org/downloads
2. Extract the archive in `C: \\ Kafka`
3. Open a terminal to start Zookeeper:

```bash
cd C:\\kafka
.\\bin\\windows\\zookeeper-server-start.bat .\\config\\zookeeper.properties
```
![image](https://github.com/user-attachments/assets/bf37e1b3-3565-4c8a-a697-8a0dad68fb63)

4. In another terminal, start Kafka :
```bash
.\\bin\\windows\\kafka-server-start.bat .\\config\\server.properties
```
![image](https://github.com/user-attachments/assets/f3a4bdc9-20d1-44d2-b37c-ef2fedf3916c)

---
## 2️⃣ Creation of a topic

Create a kafka topic called IoT-Topic :
```bash
.\bin\windows\kafka-topics.bat --create --topic iot-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
![image](https://github.com/user-attachments/assets/a29948e0-af7a-47cd-a68f-2b989a102f37)

List the topics :
```bash
.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
```
![image](https://github.com/user-attachments/assets/bccba3a3-b6da-4ecf-a775-6a3ed09a86b9)

---
## 3️⃣ Exemple Producteur Consommateur

### 🟢 Producer :

```bash
.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic iot-topic
```
Write a message and press Entrance.

![image](https://github.com/user-attachments/assets/f9ebdc59-1225-4652-ac93-156d48193004)

### 🔵 Consumer :

```bash
.\bin\\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic iot-topic --from-beginning
```
![image](https://github.com/user-attachments/assets/18f6b7f2-62f3-4e75-9dc3-48e6730c1635)

---
## 4️⃣ Configuration of several brokers

1. Duplicate the Server file.Properties: 

  - `Server-1.Properties`

  - `Server-2. Properties`

2. Modify each file:

  - `Broker.id = 1/2`

  - `List = complaint: //: 9093/9094`

  - `log.DIRS = C:/KAFKA/KAFKA-LOGS-1 and KAFKA-LOGS-2`

3. Start Each Broker in a terminal:

```bash
.\bin\windows\kafka-server-start.bat .\config\server-1.properties
```
![image](https://github.com/user-attachments/assets/d4d46d87-e94e-4789-bcc9-af0ac3f20984)

```bash
.\bin\windows\kafka-server-start.bat .\config\server-2.properties
```
![image](https://github.com/user-attachments/assets/bb5908a8-e43f-42be-8411-30cae4c83978)

4. Create a replicated topic :
```bash
.\bin\windows\kafka-topics.bat --create --topic replicated-topic --bootstrap-server localhost:9093 --partitions 1 --replication-factor 2
```
![image](https://github.com/user-attachments/assets/760f15f3-45cd-4c56-9692-b5af7eac22db)

---
## 5️⃣ Projet IoT + Kafka

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










