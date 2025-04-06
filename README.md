# TP N°6 - NoSQL Databases with Cassandra

## 📌 Objective
Create a NoSQL database using Cassandra to store and query information about restaurants and their health inspections in New York City.

---

## 🛠️ Installation & Execution

### Via Docker:
```bash
docker exec -it cassandra-container cqlsh
```

- -it: for interactive terminal
- cqlsh: Cassandra command-line interface

## 🧱 Creating the Keyspace (Database)
```bash
CREATE KEYSPACE IF NOT EXISTS resto_NY
WITH REPLICATION = { 'class': 'SimpleStrategy', 'replication_factor': 1 };

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
-- 2. List restaurant names only
```bash
SELECT name FROM Restaurant;
```
-- 3. Get name and borough of a specific restaurant
```bash
SELECT name, borough FROM Restaurant WHERE id = 41569764;
```
-- 4. Get inspection dates and grades for a restaurant
```bash
SELECT inspectiondate, grade FROM Inspection WHERE idrestaurant = 41569764;
```
-- 5. Get names of restaurants serving French cuisine
```bash
SELECT name FROM Restaurant WHERE cuisinetype = 'French';
```
-- 6. Get names of restaurants in Brooklyn
```bash
SELECT name FROM Restaurant WHERE borough = 'BROOKLYN' ALLOW FILTERING;
```
-- 7. Grades and scores of a restaurant with score ≥ 10
```bash
SELECT grade, score FROM Inspection WHERE idrestaurant = 41569764 AND score >= 10 ALLOW FILTERING;
```
-- 8. Grades for inspections with score > 30
```bash
SELECT grade FROM Inspection WHERE score > 30 ALLOW FILTERING;
```
-- 9. Count of the previous query
```bash
SELECT count(*) FROM Inspection WHERE score > 30 ALLOW FILTERING;
```
