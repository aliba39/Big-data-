import pandas as pd
import time
import psutil

def process_with_chunksize(file_path, chunk_size=100000):
    print("Processing with chunksize...")
    start_time = time.time()
    mem_before = psutil.Process().memory_info().rss / (1024 ** 2)
    
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        print(chunk.shape)

    mem_after = psutil.Process().memory_info().rss / (1024 ** 2)
    elapsed_time = time.time() - start_time
    print(f"Processing completed! Time: {elapsed_time:.2f} sec | Memory: {mem_after - mem_before:.2f} MB")
    
    return elapsed_time, mem_after - mem_before

if __name__ == "__main__":
    process_with_chunksize("./ecommerce_data/ecommerce_data.csv")
