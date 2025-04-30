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
├── wordcount-spark/
│   ├── src/
│   │   └── main/
|   |       └── java/spark/batch/tp21/WordCountTask.java
|   |       └── recources
│   ├── pom.xml
│   └── target/wordcount-spark.jar
│
├── stream/
│   ├── src/
│   │   └── main/
|   |       └── java/spark/streaming/tp22/Stream.java
|   |       └── recources
│   ├── pom.xml
│   └── target/stream-1.jar
│
├── input/
│   └── purchases.txt
├── README.md
```

---

## 🚀 Usage
## 🧪 Verifying Spark Installation with spark-shell
### 1. Start Hadoop Cluster (using Docker)

- Run the following commands on your host machine:
```bash
docker start hadoop-master hadoop-worker1 hadoop-worker2
docker exec -it hadoop-master bash
./start-hadoop.sh
```
![image](https://github.com/user-attachments/assets/81bff7da-4d30-4023-ac06-5f33fefc1644)

### 2. Check that all Hadoop daemons are running:
```bash
jps
```
![image](https://github.com/user-attachments/assets/33c7ebb5-0bd3-4a85-b35e-108a4e9e821c)

### 3. Create a test file inside the master container:
```bash
echo -e 'Hello Spark Wordcount!\\nHello Hadoop Also :)' > file1.txt
hdfs dfs -put file1.txt
```
### 4. Launch Spark Shell to test:
```bash
spark-shell
```
![لقطة شاشة 2025-04-30 152645](https://github.com/user-attachments/assets/7f23ee85-3a41-483b-bfbb-a6ac53ab850d)

### 5. Run this Scala code line by line inside the shell:
```bash
val lines = sc.textFile("file1.txt")
val words = lines.flatMap(_.split("\\\\s+"))
val wc = words.map(w => (w, 1)).reduceByKey(_ + _)
wc.saveAsTextFile("file1.count")
```
![لقطة شاشة 2025-04-30 152705](https://github.com/user-attachments/assets/aaea4ace-b532-46c2-ba0a-576017dd4856)

### 6. Download the output from HDFS:
```bash
hdfs dfs -get file1.count
```
![لقطة شاشة 2025-04-30 152838](https://github.com/user-attachments/assets/b7162186-51f0-4bab-87f4-d60386dd49fa)

### 7. Check output:
- You should see files like part-00000 and part-00001 containing word counts.
```bash
hdfs dfs -tail file1.count
```
![لقطة شاشة 2025-04-30 152952](https://github.com/user-attachments/assets/1671d78d-ff4a-44d7-bd0e-4623619cf4f3)

---

## 📦 Part 1: Batch Processing with Spark

### Compile the Java Project

```bash
cd batch/
mvn package
```
![لقطة شاشة 2025-04-30 161027](https://github.com/user-attachments/assets/307ab74b-f57d-4c6a-a579-cc80dd50c595)

### Copy the .jar to the master container

```bash
docker cp target/wordcount-spark.jar hadoop-master:/root/
```
![لقطة شاشة 2025-04-30 161104](https://github.com/user-attachments/assets/4e28f6f5-57c3-4224-a0bd-06f86d3b8d52)

### Run the job in local mode

```bash
hdfs dfs -mkdir -p input

hdfs dfs -put purchases.txt

spark-submit --class spark.batch.tp21.WordCountTask \
             --master local \
             wordcount-spark.jar input/purchases.txt out-spark
```
![لقطة شاشة 2025-04-30 161758](https://github.com/user-attachments/assets/48c662e1-0df9-4e7b-a0d3-db7a550346cc)

### Run the job on YARN

```bash
spark-submit --class spark.batch.tp21.WordCountTask \
             --master yarn --deploy-mode cluster \
             wordcount-spark.jar input/purchases.txt out-spark2
```
![image](https://github.com/user-attachments/assets/935f0c4f-9db7-4bf7-956f-d0cc149b3dcc)

---

## 🔁 Part 2: Streaming Processing with Spark

### Compile the Java Project

```bash
cd streaming/
mvn package
```
![image](https://github.com/user-attachments/assets/0b8ff8d0-de78-4013-8576-442bf5177ae9)

### Copy the .jar to the master container

```bash
docker cp target/stream-1.jar hadoop-master:/root/
```
![image](https://github.com/user-attachments/assets/a0715c8c-37c1-4a54-a3c5-2aad7a3bfa8b)

### Install netcat (nc) on the container

```bash
apt update
apt install netcat
```
![image](https://github.com/user-attachments/assets/737fd5d4-4d80-4eb2-85b5-954f0c958e23)

### Create a local stream

```bash
nc -lk 9999
```
![image](https://github.com/user-attachments/assets/1350e9ec-52b1-438a-8fcd-35128e18d753)

### Run the streaming process

```bash
spark-submit --class spark.streaming.tp22.Stream \
             --master local \
             stream-1.jar > out
```
![لقطة شاشة 2025-04-30 194847](https://github.com/user-attachments/assets/96d90f43-f4e3-4ba8-a3f5-58469eb30b61)

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
