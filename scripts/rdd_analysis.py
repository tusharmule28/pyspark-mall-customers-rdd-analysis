from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Mall Customers RDD Analysis") \
    .getOrCreate()

# HDFS CSV Path
csv_path = "hdfs:///data/Mall_Customers.csv"

# Load file into RDD
rdd = spark.sparkContext.textFile(csv_path)

# Extract header
header = rdd.first()

# Remove header (NARROW transformation)
data_rdd = rdd.filter(lambda row: row != header)

print("\n--- RAW RDD SAMPLE ---")
print(data_rdd.take(5))

# ---------------------------
# NARROW TRANSFORMATIONS
# ---------------------------

mapped_rdd = data_rdd.map(lambda line: line.split(","))

female_rdd = mapped_rdd.filter(lambda row: row[1] == "Female")
print("\n--- FEMALE CUSTOMERS SAMPLE ---")
print(female_rdd.take(5))

# ---------------------------
# WIDE TRANSFORMATIONS
# ---------------------------

gender_pairs = mapped_rdd.map(lambda row: (row[1], 1))
gender_count = gender_pairs.reduceByKey(lambda a, b: a + b)

print("\n--- CUSTOMER COUNT BY GENDER ---")
print(gender_count.collect())

age_pairs = mapped_rdd.map(lambda row: (int(row[2]) // 10 * 10, 1))
age_group_count = age_pairs.reduceByKey(lambda a, b: a + b)

print("\n--- CUSTOMER COUNT BY AGE GROUP ---")
print(age_group_count.collect())

# Actions
print("\n--- ACTIONS ---")
print("Total rows:", data_rdd.count())
print("First row:", data_rdd.first())
print("Sample rows:", mapped_rdd.take(5))

spark.stop()
