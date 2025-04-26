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

## 3. HDFS Operations
```bash
# Create HDFS directory and upload data
hdfs dfs -mkdir -p /user/root/input
hdfs dfs -put purchases.txt input
hdfs dfs -ls input  # Verify upload
```
![image](https://github.com/user-attachments/assets/e1a36270-ff00-4654-a51a-5c69bd74d9ab)
# 🖥️ Run WordCount MapReduce Job
## 1. Build the Project
```bash
mvn clean package  # Generates JAR in target/
```
![image](https://github.com/user-attachments/assets/517406b7-ee95-4647-95f2-d4497dd11208)
## 2. Copy JAR to Hadoop Master
```bash
docker cp target/wordcount-1.0-SNAPSHOT-jar-with-dependencies.jar hadoop-master:/root/wordcount.jar
```
![لقطة شاشة 2025-04-26 090359](https://github.com/user-attachments/assets/f7ed7045-b056-4302-ab7e-fe3b5b6e7eef)

## 3. Execute the Job
```bash
# Inside the Hadoop master container
hadoop jar wordcount.jar input output

# View results
hdfs dfs -cat output/part-r-00000
```

# 📊 Monitoring
HDFS UI: http://localhost:9870

YARN ResourceManager: http://localhost:8088

Worker Nodes:

Worker 1: `http://localhost:8041`

Worker 2: `http://localhost:8042`

# 🚨 Troubleshooting
Windows Users: Set `HADOOP_HOME` environment variable and add `%HADOOP_HOME%\bin` to `PATH`.

Port Conflicts: Ensure ports `9870`, `8088`, `8040-8042` are free.

HDFS Permissions: Always create `/user/root` before working with HDFS.

# 📂 Project Structure
```bash
.
├── src/
│   └── main/java/hadoop/mapreduce/
│       ├── tp1/
│       │   ├── TokenizerMapper.java    # Mapper class
│       │   ├── IntSumReducer.java      # Reducer class
│       │   └── WordCount.java          # Driver class
├── target/                             # Compiled JAR
├── pom.xml                            # Maven dependencies
├── resources/
│   └── input/                         # Sample input files
└── .vscode
    └── launch.json
```
![image](https://github.com/user-attachments/assets/e72b1e91-9cf2-4cac-bd3f-1cbf27254285)
















