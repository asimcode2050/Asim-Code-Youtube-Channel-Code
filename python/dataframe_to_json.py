import pandas as pd

data = {
        'id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
                'hobbies': [['reading', 'hiking'], ['cooking'], ['gaming', 'swimming']]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

json_output = df.to_json(orient='records')

print("\nJSON Output:")
print(json_output)

