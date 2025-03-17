import boto3
import random
from datetime import datetime, timedelta
import uuid

# Create a DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Specify the name of your DynamoDB table
table_name = 'SalesData'  # Replace with your table name
table = dynamodb.Table(table_name)

# Sample data for categories, products, and countries
countries = ['USA', 'Canada', 'Germany', 'India', 'UK', 'Australia']
products = [
    {'product_id': 'P001', 'product_name': 'Laptop'},
    {'product_id': 'P002', 'product_name': 'Smartphone'},
    {'product_id': 'P003', 'product_name': 'Headphones'},
    {'product_id': 'P004', 'product_name': 'Tablet'},
    {'product_id': 'P005', 'product_name': 'Smartwatch'}
]

# Function to generate a random sale
def generate_sale():
    country = random.choice(countries)
    customer_id = random.randint(1000, 9999)  # Random customer ID between 1000 and 9999
    order_date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%d/%m/%Y')
    product = random.choice(products)
    discount = random.randint(5, 20)  # Random discount between 5% and 20% (integer)
    sales = random.randint(50, 1000)  # Random sales value between 50 and 1000 (integer)
    profit = sales * (100 - discount) // 100  # Profit after applying discount (integer)
    
    sale_data = {
        'order_id': str(uuid.uuid4()),  # Generate unique order_id using UUID
        'category': country,
        'customer_id': customer_id,
        'order_date': order_date,
        'product_id': product['product_id'],
        'product_name': product['product_name'],
        'discount': discount,
        'sales': sales,
        'profit': profit
    }
    
    return sale_data

# Insert multiple records into the DynamoDB table
def insert_sales_data(num_records):
    for i in range(num_records):
        sale_data = generate_sale()  # Generate sale with unique order_id
        table.put_item(Item=sale_data)
        print(f"Inserted Order ID: {sale_data['order_id']} into DynamoDB.")

# Example: Insert 10 records
insert_sales_data(10)
