# convert_and_compare.py
import pandas as pd
import os

print("Reading CSV file into memory...")
df = pd.read_csv('transactions.csv')

print("Converting to Parquet formats...")
if not os.path.exists('transactions.snappy.parquet'):
	df.to_parquet('transactions.snappy.parquet', engine='pyarrow', compression='snappy')
	print("Created transactions.snappy.parquet")
else:
	print("transactions.snappy.parquet already exists, skipping.")
 
if not os.path.exists('transactions.gzip.parquet'):
	df.to_parquet('transactions.gzip.parquet', engine='pyarrow', compression='gzip')
	print("Created transactions.gzip.parquet")
else:
	print("transactions.gzip.parquet already exists, skipping.")
 
if not os.path.exists('transactions.brotli.parquet'):
	df.to_parquet('transactions.brotli.parquet', engine='pyarrow', compression='brotli')
	print("Created transactions.brotli.parquet")
else:
	print("transactions.brotli.parquet already exists, skipping.")

csv_size = os.path.getsize('transactions.csv') / (1024**2) 
snappy_size = os.path.getsize('transactions.snappy.parquet') / (1024**2)
gzip_size = os.path.getsize('transactions.gzip.parquet') / (1024**2)
brotli_size = os.path.getsize('transactions.brotli.parquet') / (1024**2)

print("\n--- File Size Comparison ---")
print(f"{'Format':<20} | {'Size (MB)':<12} | {'Reduction'}")
print("-" * 50)
print(f"{'Original CSV':<20} | {csv_size:<12.2f} |")
print(f"{'Parquet (Snappy)':<20} | {snappy_size:<12.2f} | {100 * (1 - snappy_size/csv_size):.1f}%")
print(f"{'Parquet (Gzip)':<20} | {gzip_size:<12.2f} | {100 * (1 - gzip_size/csv_size):.1f}%")
print(f"{'Parquet (Brotli)':<20} | {brotli_size:<12.2f} | {100 * (1 - brotli_size/csv_size):.1f}%")