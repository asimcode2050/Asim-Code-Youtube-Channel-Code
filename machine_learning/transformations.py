import pandas as pd
data = {
    'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
    'Sales': [150, 200, 220, 180, 160, 190, 180, 210],
    'Month': ['January', 'January', 'January', 'January', 'February', 'February', 'February', 'February']
}

df = pd.DataFrame(data)
sum_sales = df.groupby('Product')['Sales'].sum()
agg_sales = df.groupby('Product')['Sales'].agg(['sum', 'mean', 'count'])
custom_agg = df.groupby('Region')['Sales'].agg(lambda x: x.sum() - 10)
sales_by_product_month = df.groupby(['Product', 'Month'])['Sales'].sum()
reset_index_agg = sales_by_product_month.reset_index()
print("Sum of sales by product:")
print(sum_sales)
print("\nMultiple aggregation functions (sum, mean, count) for sales by product:")
print(agg_sales)
print("\nCustom aggregation (sum of sales minus 10) by region:")
print(custom_agg)
print("\nSales by product and month:")
print(sales_by_product_month)
print("\nSales by product and month with reset index:")
print(reset_index_agg)
