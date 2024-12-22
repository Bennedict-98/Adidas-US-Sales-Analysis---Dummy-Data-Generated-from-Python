import pandas as pd
import random
import os

# Print the current working directory
print(os.getcwd())

# Set the number of rows you want
num_rows = 12000

# Sample data
retailers = ['RetailCo', 'ShopMart', 'SuperShop']
regions = ['East', 'West', 'North', 'South']
states = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
    'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
    'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
    'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
    'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
    'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
    'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
    'Wisconsin', 'Wyoming'
]
products = [
    "Men's Apparel", "Men's Athletic Footwear", "Men's Street Footwear",
    "Women's Apparel", "Women's Athletic Footwear", "Women's Street Footwear"
]
sales_methods = ['In Store', 'Online', 'Outlet']

data = {
    'Retailer': [random.choice(retailers) for _ in range(num_rows)],
    'Retailer ID': [f'R{str(random.randint(1, 100)).zfill(3)}' for _ in range(num_rows)],
    'Invoice Date': pd.date_range(start='2023-01-01', periods=num_rows, freq='H').strftime('%m/%d/%Y'),
    'Region': [random.choice(regions) for _ in range(num_rows)],
    'State': [random.choice(states) for _ in range(num_rows)],
    'City': [random.choice(states) for _ in range(num_rows)],  # Using states as cities
    'Product': [random.choice(products) for _ in range(num_rows)],
    'Price per Unit': [random.uniform(10, 300) for _ in range(num_rows)],
    'Units Sold': [random.randint(1, 100) for _ in range(num_rows)],
    'Total Sales': [random.uniform(100, 10000) for _ in range(num_rows)],
    'Operating Profit': [random.uniform(50, 2000) for _ in range(num_rows)],
    'Operating Margin': [round(random.uniform(0.05, 0.2), 2) for _ in range(num_rows)],
    'Sales Method': [random.choice(sales_methods) for _ in range(num_rows)],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Export to Excel
df.to_excel('dummy_data.xlsx', index=False)





