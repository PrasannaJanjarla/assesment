import boto3
import csv

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'SalesData'  # Replace with your DynamoDB table name
table = dynamodb.Table(table_name)

# Function to scan the DynamoDB table and write the items to a CSV file
def export_to_csv():
    # Scan the table to get all the items
    response = table.scan()
    items = response['Items']

    # Open a CSV file to write data
    with open('exported_sales_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Write header row (this assumes the columns you want are present in every item)
        if items:
            header = items[0].keys()  # Use the keys of the first item as headers
            writer.writerow(header)

            # Write all items to the CSV
            for item in items:
                writer.writerow(item.values())

    print("Data has been successfully exported to 'exported_sales_data.csv'.")

# Call the function to export data
export_to_csv()
