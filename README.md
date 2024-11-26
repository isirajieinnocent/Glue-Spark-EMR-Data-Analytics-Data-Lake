This project involves data processing and analysis to compute the gross profit of sales transactions. The following technologies and processes are used:

PySpark: The project utilizes PySpark, a Python API for Apache Spark, which is an open-source big data processing framework. PySpark allows you to perform distributed data processing and analytics. We load data from multiple sources (Hive tables) into DataFrames, join them, clean the data, and compute business metrics such as gross profit.

AWS S3: The final output, a report containing the calculated gross profit, is stored as a CSV file in an Amazon S3 bucket. S3 provides scalable object storage for the data, ensuring that the reports are easily accessible and stored in a secure manner.

AWS Glue and Data Catalog:

AWS Glue Crawler: In a production scenario, you would use an AWS Glue Crawler to automate the discovery of the raw data stored in S3. The Glue Crawler would scan the raw files (such as CSV, Parquet, etc.), infer the schema (column names, data types), and catalog the data.
AWS Glue Data Catalog: The Glue Data Catalog would store the metadata information (schema, tables, partitions) for the raw data. By integrating Glue with Spark, you can easily query the data using its schema without needing to manually define it in Spark jobs. This metadata management helps improve efficiency and manage large-scale datasets effectively.
Amazon EMR (Elastic MapReduce):

EMR is a cloud-native big data processing service that can be used for scalable data processing using frameworks like Apache Spark, Hadoop, and Hive. In this project, if the data size is large or requires distributed computing, you could run the PySpark jobs on EMR clusters for high-performance computing. EMR provides a managed environment to run big data frameworks with automatic scaling, cost optimization, and integration with other AWS services like S3, Glue, and Redshift.






# Importing necessary libraries from PySpark for SparkSession and DataFrame operations
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Step 1: Set up SparkSession
# SparkSession is the entry point to using Spark for data processing. It initializes the Spark application and enables Hive support for managing large-scale data queries.
spark = SparkSession.builder.appName('data_processing').enableHiveSupport().getOrCreate()

# Step 2: Set the database context to use the sales-billig database in Hive
# This step tells Spark to work with a specific database (sales-billig) in Hive, where all the tables we need are stored.
spark.sql("USE `sales-billig`")

# Step 3: Load the tables into DataFrames
# The next lines of code load three tables: 'billing_processed_pro', 'unit_sold', and 'production_cost' from the Hive database into DataFrames.
bills_df = spark.table('billing_processed_pro')
bills_df = bills_df.na.drop()  # Drop any rows containing null values to clean the data

unit_sold_df = spark.table('unit_sold')
unit_sold_df = unit_sold_df.na.drop()  # Drop rows with null values for the unit sold data

production_cost_df = spark.table('production_cost')
production_cost_df = production_cost_df.na.drop()  # Drop rows with null values for production cost data

# Step 4: Join the DataFrames to combine the necessary information
# We join the three DataFrames on relevant columns to combine the data needed for gross profit calculation.
# This join operation combines 'billing_processed_pro' with 'unit_sold' and 'production_cost' based on the common keys.
joined_df = (
    bills_df.join(unit_sold_df, bills_df.id == unit_sold_df.company_id)  # Join on company_id
    .drop('company_id')  # Drop company_id after the join since it's no longer needed
    .join(production_cost_df, bills_df.item_sold == production_cost_df.item)  # Join on item sold
    .drop(bills_df.item_sold)  # Drop item_sold column from bills_df
    .drop(unit_sold_df.item_type)  # Drop item_type from unit_sold_df
)

# Step 5: Calculate gross profit
# A new column is created in the joined DataFrame to calculate the gross profit. The formula is:
# gross_profit = bill_amount - (units_sold * cost_per_unit_usd)
gross_profit_df = joined_df.withColumn('gross_profit', (joined_df.bill_amount - (joined_df.units_sold * joined_df.cost_per_unit_usd)))

# Step 6: Select the required columns for the final result
# We select the relevant columns to include in the output dataset for further analysis.
gross_profit_df = gross_profit_df.select('id', 'company_name', 'item', 'bill_amount', 'units_sold', 'cost_per_unit_usd', 'gross_profit')

# Step 7: Write the result to S3
# The final DataFrame is written to an S3 bucket as a CSV file. The data includes the header row for easier consumption.
gross_profit_df.write.option('header', 'true').csv('s3://billing-data-lake-b/reports/gross-profit')



