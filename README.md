# pyspark-recap

30-Day PySpark Crash Course Plan (Starting 25 June 2025)

Week 1: Fundamentals

## Day 1 – Intro to Spark

Spark architecture
Install PySpark
First SparkSession

- SparkSession is the entry point for DataFrame and SQL operations.
- Master URL:

            "local[*]" runs Spark on all available cores locally.

        In production, this is something like "yarn" or "spark://host:port".

        Stop your session after the job is complete to free resources:


- ✅ Day 2 – RDD Basics

    Create RDDs
    map, filter, reduce, flatMap
    Word count example

    - RDDs are fault-tolerant — Spark can recompute lost partitions using lineage.
    - Lazy Evaluation — nothing runs until you call an action.
    - Transformations are chained, forming a DAG (Directed Acyclic Graph).
    - Use .collect() only for small datasets (it brings data to the driver).

Day 3 – DataFrames 101

Create DataFrames

Select, filter, withColumn

Load and clean CSV

Day 4 – Spark SQL

Create temp views

Run SQL queries

Practice joins

Day 5 – DataFrame Operations

groupBy, agg, orderBy

All join types

Day 6 – Data Types & UDFs

Complex types: struct, array

Register and use UDFs

Day 7 – Mini Project

Taxi trip data

Clean, analyze, SQL queries

Week 2: Intermediate PySpark

Day 8 – Partitioning & Persistence

.repartition(), .coalesce()

Caching strategies

Day 9 – Working with Time

to_date, date_format, datediff

Time series analysis

Day 10 – Handling Nulls & Duplicates

dropna, fillna, dropDuplicates

Day 11 – Writing Data

Write to Parquet, JSON, CSV

partitionBy, save modes

Day 12 – Aggregations at Scale

Window functions

rollup, cube, pivot

Day 13 – PySpark with AWS S3

hadoop-aws setup

Read/write from S3

Day 14 – Mini Project

Weather data ingestion and analysis

Week 3: Advanced Topics

Day 15 – Performance Tuning I

DAG, stages, Catalyst optimizer

Use .explain()

Day 16 – Performance Tuning II

Serialization

Broadcast joins

Day 17 – Debugging & Logging

Spark logs overview

Using log4j

Day 18 – Dockerized PySpark

Create Docker container

Run PySpark script inside

Day 19 – Airflow Integration

Build Airflow DAG

Trigger Spark job

Day 20 – Interop with Pandas

Use .toPandas()

pandas_udf

Day 21 – Mini Project

Full ETL pipeline with Airflow + Docker

Week 4: Streaming & Machine Learning

Day 22 – Nested JSON

Read multi-line JSON

Explode and flatten data

Day 23 – Kafka & Streaming

Read from Kafka

Structured Streaming basics

Day 24 – Streaming Transformations

Watermark, windowed aggregations

Day 25 – MLlib Basics

ML pipeline: StringIndexer, VectorAssembler

Classification example

Day 26 – Hyperparameter Tuning

ParamGridBuilder, CrossValidator

Day 27 – Model Deployment

Save/load models

Batch inference
