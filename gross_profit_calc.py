from pyspark.sql import  SparkSession
from pyspark.sql.functions import *
from pyspark.sql.functions import col


spark = SparkSession.builder.appName('data_processing').enableHiveSupport().getOrCreate()

spark.sql("USE `sales-billig`")

bills_df = spark.table('billing_processed_pro')
bills_df = bills_df.na.drop()
#bills_df.show()

unit_sold_df = spark.table('unit_sold')
unit_sold_df =unit_sold_df.na.drop()
#unit_sold_df.show()

production_cost_df = spark.table('production_cost')
production_cost_df =production_cost_df.na.drop()
#production_cost_df.show()

joined_df = (
    bills_df.join(unit_sold_df, bills_df.id == unit_sold_df.company_id)
    .drop('company_id')
    .join(production_cost_df, bills_df.item_sold == production_cost_df.item)
    .drop(bills_df.item_sold)
    .drop(unit_sold_df.item_type)

)

#joined_df.show()


gross_profit_df = joined_df.withColumn('gross_profit',(joined_df.bill_amount - (joined_df.units_sold * joined_df.cost_per_unit_usd)))

gross_profit_df = gross_profit_df.select('id', 'company_name', 'item', 'bill_amount', 'units_sold','cost_per_unit_usd','gross_profit')

#gross_profit_df.show()

gross_profit_df.write.option('header','true').csv('s3://billing-data-lake-b/reports/gross-profit')
















