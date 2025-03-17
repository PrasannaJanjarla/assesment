1. Set Up the Datastore
    I chose Amazon DynamoDB because it’s highly scalable and flexible, perfect for my needs. I created a table named SalesData with these fields:

Attribute Type Description order_id String Unique ID for each order category String Country where the sale happened customer_id Number Randomly generated customer ID order_date String Date of order (e.g., 15/03/2025) product_id String ID of the product sold product_name String Name of the product discount Number Discount percentage sales Number Sales amount before discount profit Number Profit made after applying the discount

To make things easier, I automated the table creation process by writing a script, datastore_setup.py.

2. Ingested Data into DynamoDB
   Next, I developed a Python script, data_ingest.py, to generate mock sales data. This script created records with key fields like:

Attribute Type Description order_id String Unique ID for each order category String Country where the sale happened customer_id Number Randomly generated customer ID order_date String Date of order (e.g., 15/03/2025) product_id String ID of the product sold product_name String Name of the product discount Number Discount percentage sales Number Sales amount before discount profit Number Profit made after applying the discount

I then used the script to insert this sample data into the SalesData table, ensuring the data was stored efficiently for later analysis.

3. Exported Data for Analysis
   Once the data was in DynamoDB, I wrote another Python script to export it into a CSV file named exported_sales_data.csv. I ensured the exported data was structured properly so it could be easily used with visualization tools.

5. Created a Tableau Dashboard for Visualization
   Finally, I took the CSV file and loaded it into Tableau to design an interactive dashboard.
   The dashboard featured:

Sales trends over time.

Sales distribution by product category.

A geographic heatmap showing sales by region.

To make the visualization accessible, I:

Wrote a guide (visualization.md) explaining how to view and interact with the dashboard.

Shared a screenshot (dashboard.png) of the final dashboard for reference.
