# TP N°6 - NoSQL Databases with Cassandra

## 📌 Objective
Create a NoSQL database using Cassandra to store and query information about restaurants and their health inspections in New York City.

---

## 🛠️ Installation & Execution

### Via Docker:
  1. Open PowerShell or CMD and pull Cassandra image:
```bash
docker pull cassandra
```
  2. Start a Cassandra container:
```bash
docker run --name cassandra-container -p 9042:9042 -d cassandra
```
  3. Access the CQL shell (cqlsh):
```bash
docker exec -it cassandra-container cqlsh
```

- -it: for interactive terminal
- cqlsh: Cassandra command-line interface

## 🧱 Creating the Keyspace (Database)
```bash
CREATE KEYSPACE IF NOT EXISTS resto_NY
WITH REPLICATION = { 'class': 'SimpleStrategy', 'replication_factor': 1 };
```
```bash
USE resto_NY;
```

## 🗃️ Creating the Tables

### Restaurant Table:
```bash
CREATE TABLE Restaurant (
  id INT,
  Name VARCHAR,
  borough VARCHAR,
  BuildingNum VARCHAR,
  Street VARCHAR,
  ZipCode INT,
  Phone TEXT,
  CuisineType VARCHAR,
  PRIMARY KEY (id)
);
```
- Creating index on CuisineType:

```bash
CREATE INDEX fk_Restaurant_cuisine ON Restaurant (CuisineType);
```

---

### Inspection Table:
```bash
CREATE TABLE Inspection (
  idRestaurant INT,
  InspectionDate DATE,
  ViolationCode VARCHAR,
  ViolationDescription VARCHAR,
  CriticalFlag VARCHAR,
  Score INT,
  Grade VARCHAR,
  PRIMARY KEY (idRestaurant, InspectionDate)
);
```	
- Creating index on Grade :

```bash
CREATE INDEX fk_Inspection_Restaurant ON Inspection (Grade);
```	
## 📥 Importing the Data
### Steps:
  1. Extract the restaurants.zip file
  2. Copy the .csv files into the Docker container:

```bash
docker cp path-to-file/restaurants.csv container-ID:/
docker cp path-to-file/restaurants_inspections.csv container-ID:/
```	
  3. Use COPY command inside cqlsh:
```bash	
USE resto_NY;
```

```bash
COPY Restaurant (id, name, borough, buildingnum, street, zipcode, phone, cuisinetype)
FROM '/restaurants.csv' WITH DELIMITER=',';

COPY Inspection (idrestaurant, inspectiondate, violationcode, violationdescription, criticalflag, score, grade)
FROM '/restaurants_inspections.csv' WITH DELIMITER=',';
```
  4. Verify the data count:
```bash 
SELECT count(*) FROM Restaurant;
SELECT count(*) FROM Inspection;
```	

## 🔍 Useful CQL Queries

-- 1. List all restaurants
```bash
SELECT * FROM Restaurant;
```
![image](https://github.com/user-attachments/assets/18218934-5cd0-46dc-b031-28e3114c4fa3)

-- 2. List restaurant names only
```bash
SELECT name FROM Restaurant;
```
![image](https://github.com/user-attachments/assets/82ca7c97-63ad-4e4a-9d71-0e9b0f7fc227)

-- 3. Get name and borough of a specific restaurant
```bash
SELECT name, borough FROM Restaurant WHERE id = 41569764;
```
![image](https://github.com/user-attachments/assets/f058f3d8-4873-4691-97fd-4b8fd78be41f)

-- 4. Get inspection dates and grades for a restaurant
```bash
SELECT inspectiondate, grade FROM Inspection WHERE idrestaurant = 41569764;
```
![image](https://github.com/user-attachments/assets/2369896b-cf76-4d84-9df9-ef1c4eeb90aa)

-- 5. Get names of restaurants serving French cuisine
```bash
SELECT name FROM Restaurant WHERE cuisinetype = 'French';
```
![image](https://github.com/user-attachments/assets/c13274c6-61ec-4f86-9c10-c5427cff592e)

-- 6. Get names of restaurants in Brooklyn
```bash
SELECT name FROM Restaurant WHERE borough = 'BROOKLYN' ALLOW FILTERING;
```
![image](https://github.com/user-attachments/assets/e666ce6e-9c32-4027-a14b-7289179a8dd3)

-- 7. Grades and scores of a restaurant with score ≥ 10
```bash
SELECT grade, score FROM Inspection WHERE idrestaurant = 41569764 AND score >= 10 ALLOW FILTERING;
```
![image](https://github.com/user-attachments/assets/e4281f9b-8823-463f-8cf9-0611b6ae2c2c)

-- 8. Grades for inspections with score > 30
```bash
SELECT grade FROM Inspection WHERE score > 30 ALLOW FILTERING;
```
![image](https://github.com/user-attachments/assets/cd00ade3-b484-4da6-8de8-5a9c7846ad52)

-- 9. Count of the previous query
```bash
SELECT count(*) FROM Inspection WHERE score > 30 ALLOW FILTERING;
```
![image](https://github.com/user-attachments/assets/41a75e0d-3020-49dd-ac41-d721922b6b55)

