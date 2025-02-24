import pandas as pd
import gzip
import time
import psutil

def process_with_compression(file_path, chunk_size=100000):
    print("Processing with gzip compression...")

    start_time = time.time()
    mem_before = psutil.Process().memory_info().rss / (1024 * 1024)

    total_rows = 0
    with gzip.open(file_path, "rt", encoding="utf-8") as f:
        for chunk in pd.read_csv(f, chunksize=chunk_size):
            total_rows += len(chunk)  # عدّ الصفوف فقط بدون تخزينها
            print(f"Processed {total_rows} records...")

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss / (1024 * 1024)

    print("Processing completed!")
    return round(end_time - start_time, 2), round(mem_after - mem_before, 2)

if __name__ == "__main__":
    time_taken, mem_used = process_with_compression("./ecommerce_data/ecommerce_data.csv.gz")
    print(f"Time: {time_taken} sec | Memory: {mem_used} MB")
