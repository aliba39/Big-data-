import os
import gzip
import shutil
import pandas as pd
import download_data
import process_chunksize
import process_dask
import process_compression
import sys

sys.stdout.reconfigure(encoding='utf-8')

csv_file = "./ecommerce_data/2019-Oct.csv"
gzip_file = csv_file + ".gz"
results = {}

if not os.path.exists(csv_file):
    print("Downloading dataset...")
    download_data.download_dataset()

if not os.path.exists(gzip_file):
    print("Compressing file to gzip...")
    with open(csv_file, "rb") as f_in:
        with gzip.open(gzip_file, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    print("Compression completed!")

print("\nProcessing data using different methods...\n")

time_chunksize, mem_chunksize = process_chunksize.process_with_chunksize(csv_file)
results["chunksize"] = (time_chunksize, mem_chunksize)

time_dask, mem_dask = process_dask.process_with_dask(csv_file)
results["dask"] = (time_dask, mem_dask)

time_compression, mem_compression = process_compression.process_with_compression(gzip_file)
results["compression"] = (time_compression, mem_compression)

results_df = pd.DataFrame.from_dict(results, orient="index", columns=["Time (Seconds)", "Memory (MB)"])
results_df.index.name = "Method"
results_csv_path = "./comparison_results.csv"
results_df.to_csv(results_csv_path, encoding="utf-8")

print("\nComparison Results:")
print(results_df)

print(f"\nResults saved in {results_csv_path}")
