
import pandas as pd
data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]
df = pd.DataFrame(data)
schema = pd.io.json.build_table_schema(df)
print(schema)
