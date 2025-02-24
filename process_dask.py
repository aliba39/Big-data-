import dask.dataframe as dd
import time
import psutil

def process_with_dask(file_path):
    print("Processing with Dask...")

    start_time = time.time()
    mem_before = psutil.Process().memory_info().rss / (1024 ** 2)

    df = dd.read_csv(file_path)

    row_count = df.shape[0].compute()  
    col_count = df.shape[1]  

    mem_after = psutil.Process().memory_info().rss / (1024 ** 2)
    elapsed_time = time.time() - start_time

    print(f"Processing completed! {elapsed_time:.2f} sec | {mem_after - mem_before:.2f} MB")
    print(f"Total Rows: {row_count}, Total Columns: {col_count}")

    return elapsed_time, mem_after - mem_before

if __name__ == "__main__":
    process_with_dask("./ecommerce_data/ecommerce_data.csv")
