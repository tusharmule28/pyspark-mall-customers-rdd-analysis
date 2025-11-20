Mall Customers Analysis Using PySpark (RDD)
A Beginner-Friendly Data Engineering Project Using Google Cloud Dataproc and Hadoop (HDFS)

This repository contains a complete end-to-end beginner data engineering project where I process the Mall Customers dataset using PySpark RDDs on a Hadoop-based Google Cloud Dataproc cluster.

The goal of this project is to practice core data engineering skills such as distributed processing, HDFS storage, PySpark RDD transformations, and working with real datasets.

Project Overview

This project covers the full workflow:

Uploading the dataset to HDFS

Reading CSV data using PySpark RDD

Applying narrow transformations

map

filter

Applying wide transformations

reduceByKey

Performing profile and behavior analysis

Working with a real Dataproc cluster (GCP)

This project shows my learning journey as I begin transitioning into data engineering.

Dataset Information

The project uses the Mall Customers dataset from Kaggle.

The dataset contains customer information, including age group, gender, earning level, and mall spending behavior. The data is generally used for clustering, segmentation, and behavioral analysis.

Columns in the dataset:

CustomerID — Unique customer identifier

Genre — Gender (Male or Female)

Age — Customer age

Annual Income (k$) — Annual income measured in thousands of dollars

Spending Score (1–100) — Customer spending score given by the mall

This dataset helps understand spending patterns and demographics across customer segments.

Technologies Used

PySpark RDD API

Hadoop HDFS

Google Cloud Dataproc

Jupyter Notebook

Python
