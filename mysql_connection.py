

import pandas as pd


from sqlalchemy import create_engine

# Load cleaned CSV
df = pd.read_csv("customer_shopping_behavior_cleaned.csv")

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:password@localhost/customer_shopping_db"
)

# Send data to MySQL
df.to_sql(
    name="customer_shopping",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data successfully imported into MySQL!")