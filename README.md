# MongoDB - TP N°5: CRUD Operations

This project demonstrates practical exercises using **MongoDB** to perform CRUD (Create, Read, Update, Delete) operations.

## 1. Installation
- Download and extract MongoDB to `C:\MongoDB`.
- Create the directories `C:\data` and `C:\data\db`.
- Start the MongoDB server:
  ```sh
  C:\MongoDB\bin\mongod.exe
  ```
- Open the MongoDB client:
  ```sh
  C:\MongoDB\bin\mongo.exe
  ```

## 2. Creating Database and Collection
- Select the database:
  ```js
  use info
  ```
- Insert documents into the `produits` collection:
  ```js
  db.produits.insertMany([
      {
          nom: "Macbook Pro",
          fabriquant: "Apple",
          prix: 11435.99,
          options: ["Intel Core i5", "Retina Display", "Long life battery"]
      },
      {
          nom: "Macbook Air",
          fabriquant: "Apple",
          prix: 125794.73,
          ultrabook: true,
          options: ["Intel Core i7", "SSD", "Long life battery"]
      },
      {
          nom: "Thinkpad X230",
          fabriquant: "Lenovo",
          prix: 114358.74,
          ultrabook: true,
          options: ["Intel Core i5", "SSD", "Long life battery"]
      }
  ])
  ```

## 3. Read Queries
- Retrieve all products:
  ```js
  db.produits.find().pretty()
  ```
  ![image](https://github.com/user-attachments/assets/5ea34b3f-23f6-4e78-a234-54d305059a7c)

- Recover the first product in the group:
  ```js
  db.produits.findOne()
  ```
  ![image](https://github.com/user-attachments/assets/04102e07-f271-470d-b260-b19ca9fd87ec)

- Find a specific product:
  ```js
  db.produits.findOne({nom: "Thinkpad X230"})
  db.produits.findOne({_id: ObjectId("PRODUCT_ID")})
  ```
  ![image](https://github.com/user-attachments/assets/de53c7ab-46e6-4d66-8f79-236fa0b477d1)

- Find products with a price greater than 13723 DA:
  ```js
  db.produits.find({prix: {$gt: 13723}}).pretty()
  ```
  ![image](https://github.com/user-attachments/assets/53d17270-5c9c-4ffb-89b9-978aeaaa0c97)

- Recover the first product with the ultrabook field in True:
  ```js
  db.produits.findOne({ultrabook: true})
  ```
  ![image](https://github.com/user-attachments/assets/2a9cf0c0-a191-4bff-9b15-4d2dcd4d4df9)

- Recover the first product whose name contains MacBook":
  ```js
  db.produits.findOne({nom: /Macbook/})
  ```
  ![image](https://github.com/user-attachments/assets/b433c5c6-b52a-40b9-a63b-dd7a727d9971)

- Find products whose name starts with "Macbook":
  ```js
  db.produits.find({nom: /^Macbook/}).pretty()
  ```
  ![image](https://github.com/user-attachments/assets/50929694-c4c0-4892-b50b-b1fadd36378c)

## 4. Delete Operations
- Delete all products from **Apple**:
  ```js
  db.produits.deleteMany({fabriquant: "Apple"})
  ```
- Delete a product by its **ID**:
  ```js
  db.produits.deleteOne({_id: ObjectId("PRODUCT_ID")})
  ```

---

💡 **Note**: Replace `"PRODUCT_ID"` with the actual ID retrieved using `findOne()`.  
📌 **MongoDB** is a powerful NoSQL database system for managing flexible data structures.

---

🚀 **Feel free to modify and use this template for your GitHub project!**
