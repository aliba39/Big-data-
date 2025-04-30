# TP N°9 : Traitement par Lot et Streaming avec Spark

## 🎯 Objectifs

Ce projet a pour objectif de :
- Apprendre à utiliser **Apache Spark** pour le traitement **Batch** et **Streaming**
- Mettre en œuvre des traitements parallèles sur un cluster Hadoop
- Concevoir un mini-projet Big Data intégrant Spark, Java et Docker

---

## 🛠️ Environnement et Technologies

- **Apache Spark** 3.5.0  
- **Apache Hadoop** 3.3.6  
- **Docker** (3 conteneurs : master + 2 workers)  
- **Java** 1.8  
- **Maven**  
- **VSCode** ou tout autre IDE  
- **Linux / Unix-based OS**

---

## 📁 Structure du Projet

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

## ⚙️ Lancement des conteneurs Docker

```bash
docker start hadoop-master hadoop-worker1 hadoop-worker2
docker exec -it hadoop-master bash
./start-hadoop.sh
```

---

## 📦 Partie 1 : Traitement Batch avec Spark

### Compilation du projet Java

```bash
cd batch/
mvn package
```

### Copier le .jar dans le conteneur master

```bash
docker cp target/wordcount-spark.jar hadoop-master:/root/
```

### Lancer le job en local

```bash
spark-submit --class spark.batch.tp21.WordCountTask \
             --master local \
             wordcount-spark.jar input/purchases.txt out-spark
```

### Lancer le job sur YARN

```bash
spark-submit --class spark.batch.tp21.WordCountTask \
             --master yarn --deploy-mode cluster \
             wordcount-spark.jar input/purchases.txt out-spark2
```

---

## 🔁 Partie 2 : Traitement Streaming avec Spark

### Compilation du projet Java

```bash
cd streaming/
mvn package
```

### Copier le .jar dans le conteneur master

```bash
docker cp target/stream-1.jar hadoop-master:/root/
```

### Installer netcat (nc) sur le conteneur

```bash
apt update
apt install netcat
```

### Créer un flux en local

```bash
nc -lk 9999
```

### Lancer le traitement streaming

```bash
spark-submit --class spark.streaming.tp22.Stream \
             --master local \
             stream-1.jar > out
```

Tapez des mots dans la console du terminal `nc`, et les résultats seront affichés en streaming.

---

## 📚 Fonctionnalités Clés

- Traitement de fichiers texte en mode batch
- WordCount distribué avec Spark (Scala et Java)
- Streaming en temps réel via socket TCP
- Intégration avec Docker et HDFS

---

## 🧪 Exemple de Données

Fichier `purchases.txt` contenant :

```
apple banana apple orange banana banana
```

Résultat attendu (Batch ou Streaming) :

```
apple: 2
banana: 3
orange: 1
```

---

## ✅ Auteurs

- **Ahmad Ayoub**  
- TP encadré par votre enseignant Big Data

---

## 📄 Licence

Projet académique – Licence libre à usage pédagogique
