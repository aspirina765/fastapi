from pyspark.sql import SparkSession 


class SparkJob():

    spark = SparkSession.builder().getOrCreate()


    df_carrier = spark.read.option("inferSchema", "True").json("data_blob.json")

    df_mobile = spark.read.option("inferSchema", "True").json("data_bus.json")






