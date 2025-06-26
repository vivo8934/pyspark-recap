from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("MyFirstSparkApp") \
    .master("local[*]") \
    .getOrCreate()


print(f"Spark Version: {spark.version}")

data = [("Alice", 28), ("Bob", 35), ("Catherine", 23)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()

rdd = spark.sparkContext.textFile("data/sample_text.txt")
word_counts = (
    rdd.flatMap(lambda line: line.split())
    .map(lambda word: (word.lower(), 1))
    .reduceByKey(lambda a, b: a + b)
)

for word, count in word_counts.collect():
    print(f"{word}: {count}")


spark.stop()