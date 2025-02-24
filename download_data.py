import kaggle

def download_dataset():
    print("📥 Downloading Ecommerce Churn dataset from Kaggle...")

    kaggle.api.dataset_download_files('saiparthas/ecommerce-churn', path="./ecommerce_data", unzip=True)

    print("✅ Dataset downloaded successfully!")

if __name__ == "__main__":
    download_dataset()
