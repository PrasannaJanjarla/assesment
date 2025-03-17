Data Ingestion into DynamoDB 

I created a Python script (data_ingest.py) to automatically generate and insert sample sales data into my Amazon DynamoDB table. This data included random values like countries, customer IDs, product info, discounts, sales , and profit .

Getting Started: 

Before running the script, here’s what you need to have in place:

An AWS account with DynamoDB access.

boto3 (AWS’s Python SDK) installed in your environment. You can install it using:
pip install boto3

Proper permissions (IAM) to read and write to DynamoDB.

Your AWS credentials set up. Run this in the command line to configure them:
aws configure

How the Script Works

This script is pretty straightforward! Here's what it does step by step:

Connects to DynamoDB: It initializes a DynamoDB client using boto3.resource('dynamodb').

Generates Sample Data:

Selects random countries and customers.

Picks a product from a predefined list.

Assigns an order date within the past 30 days.

Generates random values for discount, sales, and profit.

Creates a unique order_id for each record using uuid.uuid4().

Inserts Data into DynamoDB: It loops through the generated records and adds them to the table using table.put_item().

Running the Script:
python data_ingest.py

By default, it inserts 10 sample records. Want to add more? Simply adjust the function call in the script:
insert_sales_data(50)  # Inserts 50 records

What’s in Each Record?

Here’s the structure of the data added to the table:

Attribute	Type	Description
order_id	String	Unique ID for each order
category	String	Country where the sale happened
customer_id	Number	Randomly generated customer ID
order_date	String	Date of order (e.g., 15/03/2025)
product_id	String	ID of the product sold
product_name	String	Name of the product
discount	Number	Discount percentage
sales	Number	Sales amount before discount
profit	Number	Profit made after applying the discount

Once you run the script, you’ll start seeing output in the terminal like:
Inserted Order ID: f1a2b3c4-5678-9101-1121-314159265358 into DynamoDB.
Inserted Order ID: a1b2c3d4-5678-9101-1121-314159265358 into DynamoDB.

A Few Tips

Make sure the DynamoDB table already exists before you start.
You can easily modify the number of records inserted by changing the insert_sales_data() function argument.
