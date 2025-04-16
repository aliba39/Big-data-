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

List the topics :
```bash
.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
```

---
## 3️⃣ Exemple Producteur Consommateur

### 🟢 Producer :

```bash
.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic iot-topic
```
Write a message and press Entrance.

### 🔵 Consumer :

```bash
.\bin\\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic iot-topic --from-beginning
```

---
## 4️⃣ Configuration of several brokers

Duplicate the Server file.Properties: 

  - Server-1.Properties

  - Server-2. Properties












