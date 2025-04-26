# Hadoop MapReduce WordCount Example

A batch processing project demonstrating Hadoop HDFS and MapReduce, using Docker to deploy a 3-node Hadoop cluster. This project includes a classic WordCount example to count word frequencies in a text file.

## 📋 Overview
- Deploy a Hadoop cluster with 1 master and 2 worker nodes using Docker.
- Use HDFS to manage distributed file storage.
- Implement a MapReduce job (WordCount) to process data in parallel.

## 🛠️ Prerequisites
- Docker ([Install Guide](https://docs.docker.com/get-docker/))
- Java JDK 8
- Maven
- VS Code (with extensions: **Maven for Java**, **Extension Pack for Java**)

## 🚀 Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/hadoop-mapreduce-wordcount.git
cd hadoop-mapreduce-wordcount
```
## 2. Start Hadoop Cluster
```bash
# Create a Docker network
docker network create hadoop

# Launch containers
docker run -itd --net=hadoop \
  -p 9870:9870 -p 8088:8088 -p 7077:7077 -p 16010:16010 \
  --name hadoop-master --hostname hadoop-master \
  111iasfaxi/hadoop-cluster:latest

docker run -itd --net=hadoop -p 8040:8042 \
  --name hadoop-worker1 --hostname hadoop-worker1 \
  111iasfaxi/hadoop-cluster:latest

docker run -itd --net=hadoop -p 8041:8042 \
  --name hadoop-worker2 --hostname hadoop-worker2 \
  liliasfaxi/hadoop-cluster:latest  # Verify image name consistency
```
![لقطة شاشة 2025-04-26 090310](https://github.com/user-attachments/assets/080cfd27-49c8-4d0d-9a60-f971145c7b32)
```bash
# Enter the master node
docker exec -it hadoop-master bash

# Start Hadoop services
./start-hadoop.sh
```
![لقطة شاشة 2025-04-26 090328](https://github.com/user-attachments/assets/ddd1b1dd-cb29-4c83-b091-e9568f8b73e3)























