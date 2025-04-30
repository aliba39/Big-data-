# TP No. 9: Batch and Streaming Processing with Spark

## 🎯 Objectives

This project aims to:
- Learn to use **Apache Spark** for **Batch** and **Streaming** processing
- Implement parallel processing on a Hadoop cluster
- Build a mini Big Data project integrating Spark, Java, and Docker

---

## 🛠️ Environment and Technologies

- **Apache Spark** 3.5.0  
- **Apache Hadoop** 3.3.6  
- **Docker** (3 containers: master + 2 workers)  
- **Java** 1.8  
- **Maven**  
- **VSCode** or any other IDE  
- **Linux / Unix-based OS**

---

## 📁 Project Structure

```
TP-Spark/
│
├── batch/
│   ├── src/
│   │   └── main/java/spark/batch/tp21/WordCountTask.java
│   ├── pom.xml
│   └── target/wordcount-spark.jar
│
├── streaming/
│   ├── src/
│   │   └── main/java/spark/streaming/tp22/Stream.java
│   ├── pom.xml
│   └── target/stream-1.jar
│
├── input/
│   └── purchases.txt
├── README.md
```

---

## ⚙️ Starting Docker Containers

```bash
docker start hadoop-master hadoop-worker1 hadoop-worker2
docker exec -it hadoop-master bash
./start-hadoop.sh
```

---

## 📦 Part 1: Batch Processing with Spark

### Compile the Java Project

```bash
cd batch/
mvn package
```

### Copy the .jar to the master container

```bash
docker cp target/wordcount-spark.jar hadoop-master:/root/
```

### Run the job in local mode

```bash
spark-submit --class spark.batch.tp21.WordCountTask \
             --master local \
             wordcount-spark.jar input/purchases.txt out-spark
```

### Run the job on YARN

```bash
spark-submit --class spark.batch.tp21.WordCountTask \
             --master yarn --deploy-mode cluster \
             wordcount-spark.jar input/purchases.txt out-spark2
```

---

## 🔁 Part 2: Streaming Processing with Spark

### Compile the Java Project

```bash
cd streaming/
mvn package
```

### Copy the .jar to the master container

```bash
docker cp target/stream-1.jar hadoop-master:/root/
```

### Install netcat (nc) on the container

```bash
apt update
apt install netcat
```

### Create a local stream

```bash
nc -lk 9999
```

### Run the streaming process

```bash
spark-submit --class spark.streaming.tp22.Stream \
             --master local \
             stream-1.jar > out
```

Type words into the `nc` terminal console, and results will be streamed to the console.

---

## 📚 Key Features

- Batch text file processing
- Distributed WordCount with Spark (Scala and Java)
- Real-time streaming via TCP socket
- Integration with Docker and HDFS

---

## 🧪 Sample Data

File `purchases.txt` containing:

```
apple banana apple orange banana banana
```

Expected result (Batch or Streaming):

```
apple: 2
banana: 3
orange: 1
```

---

## ✅ Author

- **Ahmad Ayoub**  
- Academic project supervised by Big Data course instructor

---

## 📄 License

Academic project – Free for educational use
