import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

# Table name
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

# Wait for the table to be created
table.meta.client.get_waiter("table_exists").wait(TableName=table_name)

print(f"Table {table_name} with GSI created successfully!")
