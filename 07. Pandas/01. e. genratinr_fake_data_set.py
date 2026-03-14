import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()
np.random.seed(42)

n = 1000  # number of rows

# Generate dataset
data = {
    "id": range(1, n+1),
    "name": [fake.first_name() for _ in range(n)],
    "age": np.random.randint(18, 66, n),
    "salary": np.random.randint(30000, 120001, n),
    "department": np.random.choice(['HR', 'IT', 'Finance', 'Marketing', 'Sales'], n),
    "experience": np.random.randint(0, 41, n),
    "joining_date": [fake.date_between(start_date='-10y', end_date='today') for _ in range(n)],
    "rating": np.round(np.random.uniform(1.0, 5.0, n), 1)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("pandas_series_dataset.csv", index=False)

print("CSV file 'pandas_series_dataset.csv' created successfully!")