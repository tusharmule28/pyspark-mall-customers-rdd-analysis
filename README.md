Mall Customers Analysis Using PySpark (RDD)
A Beginner Data Engineering Project Using Google Cloud Dataproc and Hadoop (HDFS)

This repository contains an end-to-end beginner data engineering project where the Mall Customers dataset is processed using PySpark RDDs on a Hadoop-based Google Cloud Dataproc cluster.
The project is designed to build and demonstrate core data engineering skills such as distributed processing, HDFS file handling, and PySpark transformations.

1. Project Overview

This project follows a complete workflow from uploading data to HDFS to performing analysis using PySpark RDD transformations.
1.1 Steps Covered

1. Uploading the dataset to HDFS

2. Reading a CSV file using PySpark RDD

3. Applying narrow transformations
   a) map
   b) filter

4. Applying wide transformations
   a) reduceByKey

5. Analyzing customer profiles and spending behavior

6. Running everything on a Google Cloud Dataproc cluster

The project marks the beginning of my learning path as I transition into data engineering.

2. Dataset Information

The project uses the Mall Customers dataset, commonly used for customer segmentation and behavior analysis.

2.1 Dataset Columns

1. CustomerID — Unique customer identifier

2. Genre — Gender of the customer

3. Age — Age of the customer

4. Annual Income (k$) — Annual income in thousands of dollars

5. Spending Score (1–100) — Score assigned by the mall based on spending behavior

The dataset helps in understanding spending habits, demographic groups, and customer segmentation patterns.

3. Technologies Used

1. PySpark (RDD API)

2. Hadoop HDFS

3. Google Cloud Dataproc

4. Python

5. Jupyter Notebook
