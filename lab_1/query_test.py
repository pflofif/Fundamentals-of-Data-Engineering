import pandas as pd
import time

county_to_search = 'USA'
print(f"\n------ Query 1: Average transaction amount in {county_to_search}")
start_time = time.time()
df_csv = pd.read_csv('transactions.csv')
avg_amount_csv = df_csv[df_csv['country'] == county_to_search]['amount'].mean()
csv_time = time.time() - start_time
print(f"CSV Time:         {csv_time:.4f} seconds")

start_time = time.time()
df_parquet = pd.read_parquet('transactions.snappy.parquet', columns=['amount', 'country'])
avg_amount_parquet = df_parquet[df_parquet['country'] == county_to_search]['amount'].mean()
parquet_time = time.time() - start_time

print(f"Parquet Time:     {parquet_time:.4f} seconds")
print(f"Speed Improvement: {csv_time / parquet_time:.1f}x faster")


currency_to_search = 'USD'
print(f"\n------ Query 2: Count of transactions for currency {currency_to_search}")

start_time = time.time()
df_csv = pd.read_csv('transactions.csv')
count_csv = len(df_csv[df_csv['currency'] == currency_to_search])
csv_time = time.time() - start_time
print(f"CSV Time:         {csv_time:.4f} seconds")

start_time = time.time()
df_parquet = pd.read_parquet('transactions.snappy.parquet', columns=['currency'])
count_parquet = len(df_parquet[df_parquet['currency'] == currency_to_search])
parquet_time = time.time() - start_time

print(f"Parquet Time:     {parquet_time:.4f} seconds")
print(f"Speed Improvement: {csv_time / parquet_time:.1f}x faster")