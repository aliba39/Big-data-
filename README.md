# TP4 - Dockerized Application

This project demonstrates how to create a Docker image, push it to Docker Hub, and deploy multiple containers connected via a network.

## 🚀 Getting Started

### Prerequisites
- Install [Docker](https://www.docker.com/get-started)
- Create an account on [Docker Hub](https://hub.docker.com/)

---

## 🛠 Steps

### 1️⃣ Build the Docker Image
Run the following command in the project directory:

 ```bash
 docker build -t my_tp3_image .
 ```

### 2️⃣ Tag and Push the Image to Docker Hub
-Log in to Docker Hub:

 ```js
 docker login
 ```
-Tag the image:
 ```js
 docker tag my_tp3_image my_dockerhub_username/my_tp3_image:v1
 ```
-Push the image:
 ```js
 docker push my_dockerhub_username/my_tp3_image:v1
 ```

### 3️⃣ Pull the Image from Docker Hub
On another machine or after removal:

 ```js
 docker pull my_dockerhub_username/my_tp3_image:v1
 ```

### 4️⃣ Create and Run Containers
Run three instances of the image:

 ```js
 docker run -d --name container1 my_dockerhub_username/my_tp3_image:v1
 docker run -d --name container2 my_dockerhub_username/my_tp3_image:v1
 docker run -d --name container3 my_dockerhub_username/my_tp3_image:v1
 ```

5️⃣ Create a Docker Network
-To enable communication between containers:

 ```js
 docker network create my_tp3_network
 ```
-Run containers inside the network with port mapping:

 ```js
 docker run -d --name container1 --network=my_tp3_network -p 5001:5000 my_dockerhub_username/my_tp3_image:v1
 docker run -d --name container2 --network=my_tp3_network -p 5002:5000 my_dockerhub_username/my_tp3_image:v1
 docker run -d --name container3 --network=my_tp3_network -p 5003:5000 my_dockerhub_username/my_tp3_image:v1
```

### 6️⃣ Verify Running Containers
-Check if all containers are running:

 ```js
 docker ps
 ```
-Check logs:

 ```js
 docker logs container1
 ```



