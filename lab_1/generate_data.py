import csv
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

headers = ['transaction_id', 'user_id', 'transaction_date', 'amount', 'currency', 'merchant', 'country']
currencies = ['USD', 'EUR', 'GBP', 'JPY']
countries = ['USA', 'Germany', 'Canada', 'UK', 'Australia', 'Japan']

n = int(input('Enter count of rows to generate: '))
print(f"Generating 'transactions.csv' with {n} rows...")
with open('transactions.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for i in range(n):
        writer.writerow([
            fake.uuid4(),
            random.randint(1000, 2000),
            (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat(),
            round(random.uniform(5.0, 1000.0), 2),
            random.choice(currencies),
            fake.company(),
            random.choice(countries)
        ])

print("Generation complete.")