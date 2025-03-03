<h1> Project Overview </h1>

This project aimed to automate the generation of gross profit reports by processing billing data stored in AWS. Using a combination of AWS S3, Glue, EMR, and Lake Formation, the project created an efficient and scalable data processing workflow to deliver actionable financial insights.

<h1> Architectural Diagram </h1>

![image](https://github.com/user-attachments/assets/c0df8110-a498-47e9-8c5f-6975b97fda0e)

<h1> Solution Overview </h1>

**Data Storage (S3):**

Billing data in CSV format was stored in an S3 bucket (billing-data), serving as the input for the pipeline.

**Data Crawling (AWS Glue):**

AWS Glue Crawlers parsed the CSV data, automatically discovering the schema and creating metadata tables in the Glue Data Catalog.

**Data Catalog (Glue Data Catalog):**

Stored metadata about the billing data, including table definitions and schema information, enabling efficient data management and querying.

**Data Permissions (AWS Lake Formation):**

Managed permissions and secured access to the data, ensuring only authorized users and services could access it.

**Data Processing (AWS EMR):**

An EMR cluster processed the billing data using PySpark scripts.

Calculated key metrics (e.g., units sold, production costs) to generate gross profit reports.

**Report Generation:**

Processed data was used to create gross profit reports, providing insights into financial performance.

<h1> Key Technologies </h1>

**AWS S3:** Stored raw billing data in CSV format.

**AWS Glue:** Crawled data and created metadata in the Glue Data Catalog.

**AWS EMR:** Processed data using PySpark scripts.

**AWS Lake Formation:** Managed data permissions and security.

<h1> Workflow </h1>

**Data Ingestion:**

Billing data in CSV format was uploaded to the S3 bucket (billing-data).

**Data Crawling:**

AWS Glue Crawlers parsed the CSV data and populated the Glue Data Catalog with metadata.

**Data Processing:**

The EMR cluster processed the data using PySpark scripts to calculate metrics and generate reports.

**Data Catalog & Permissions:**

The Glue Data Catalog managed metadata, while AWS Lake Formation handled permissions and security.

<h1> Challenges and Solutions </h1>

**Challenge:** Ensuring efficient data processing and timely report generation.

**Solution:** Automated data processing using AWS Glue Crawlers and an EMR cluster.

**Challenge:** Managing permissions and securing data access.

**Solution:** Implemented AWS Lake Formation for permission management and data security.

<h1> Impact </h1>

**Streamlined Data Processing: Reduced manual intervention and improved efficiency.**

**Timely Insights:** Enabled timely generation of gross profit reports for better decision-making.

**Enhanced Security:** Ensured secure data access with AWS Lake Formation.

<h1> Key Achievements </h1>

Designed an automated data processing pipeline using AWS services.

Generated gross profit reports with key financial metrics.

Improved data security and access control with AWS Lake Formation.

**This project highlights my expertise in AWS data services, PySpark programming, and data pipeline automation. It demonstrates my ability to build scalable, secure, and efficient solutions for financial data analysis**
