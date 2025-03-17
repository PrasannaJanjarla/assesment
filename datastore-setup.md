I decided to use Amazon DynamoDB to manage the SalesData table because of the platform's unmatched advantages:
1.	Effortless Scalability
 DynamoDB automatically adjusts to handle any workload big or small without me needing to intervene. This was perfect for managing fluctuating traffic and unpredictable sales data peaks.
2.	Fast Performance 
Since sales tracking relies on real-time updates and quick lookups, DynamoDB's quick response times were a lifesaver. It consistently delivers low latency reads and writes, even at large scales.
3.	Serverless Simplicity 
Being fully serverless, DynamoDB saved me the hassle of setting up and managing servers. I could focus entirely on building features instead of worrying about database infrastructure.
4.	Schema Flexibility 
With sales data, no two records are exactly the same discounts, categories, and other attributes vary. DynamoDB's flexibility as a NoSQL database was key to accommodating this dynamic structure.
Here’s how I created the SalesData table with a Global Secondary Index (GSI):
First, I used Python and AWS's SDK, boto3, to connect to DynamoDB. I decided to define order_id as the primary partition key since it uniquely identifies each order. To add extra querying power, I also created a GSI called CategoryIndex, which makes it easy to group and query sales data by categories.
The CategoryIndex uses category as its partition key, and I set it up with a projection type of ALL. This means the index includes every attribute of the table’s items—handy for flexible queries.
For both the table and the GSI, I set the read and write capacities to 5 units each. While that was sufficient for my use case, it’s easily scalable later if the workload increases.
This approach worked perfectly for tracking and analyzing sales data efficiently and in real time. The combination of a reliable primary key and the GSI made accessing and organizing sales information easy.
I ran the Python script in the command prompt using the python command, making sure my AWS CLI credentials were properly set up beforehand. The script used the boto3 library to interact with DynamoDB and handle the table creation process. This included defining the primary key (order_id), specifying attributes, setting read and write throughput, and configuring the Global Secondary Index (GSI).
Once the request was sent, DynamoDB took care of provisioning the table and making it ready for use.

Script for datastore_setup.py :


import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

table_name = "SalesData"

# Create table with a GSI
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {"AttributeName": "order_id", "KeyType": "HASH"}  # Partition Key (order_id)
    ],
    AttributeDefinitions=[
        {"AttributeName": "order_id", "AttributeType": "S"},  # Partition key attribute
        {"AttributeName": "category", "AttributeType": "S"}   # Additional attribute for GSI
    ],
    ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    GlobalSecondaryIndexes=[
        {
            "IndexName": "CategoryIndex",
            "KeySchema": [
                {"AttributeName": "category", "KeyType": "HASH"}  # Partition Key for GSI
            ],
            "Projection": {"ProjectionType": "ALL"},
            "ProvisionedThroughput": {
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
        }
    ]
)

table.meta.client.get_waiter("table_exists").wait(TableName=table_name)

print(f"Table {table_name} with GSI created successfully!")
