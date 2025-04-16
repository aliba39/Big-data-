# Create the full TP README that includes all 5 steps in a single document

full_tp_readme = """
# 🧪 TP Apache Kafka – Windows + IoT Simulation

This repository contains a complete practical lab (TP) on **Apache Kafka**, including installation, topic creation, producer-consumer demo, multiple broker configuration, and an IoT simulation project using Python.

---

## 📋 Table of Contents

1. [Installation Apache Kafka sous Windows](#installation-apache-kafka-sous-windows)
2. [Création d'un topic](#création-dun-topic)
3. [Exemple Producteur Consommateur](#exemple-producteur-consommateur)
4. [Configuration de plusieurs brokers](#configuration-de-plusieurs-brokers)
5. [Projet IoT + Kafka](#projet-iot--kafka)

---

## 1️⃣ Installation Apache Kafka sous Windows

### ✅ Prérequis

- Java JDK 8 ou plus (`java -version`)
- Python 3.7+ (pour le projet IoT)

### 📥 Étapes

1. Télécharger la version **binaire** de Kafka : https://kafka.apache.org/downloads
2. Extraire l’archive dans `C:\\kafka`
3. Ouvrir un terminal pour démarrer Zookeeper :

```bash
cd C:\\kafka
.\\bin\\windows\\zookeeper-server-start.bat .\\config\\zookeeper.properties
