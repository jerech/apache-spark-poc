from pyspark.sql import SparkSession
from pyspark.sql.functions import col, monotonically_increasing_id, size, split
from constants import KEY_WORD, FILE_NAME

spark = SparkSession.builder \
    .appName("Analisis de Texto") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()

file_path = FILE_NAME

text_file = spark.read.text(file_path)

text_file_with_index = text_file.withColumn("index", monotonically_increasing_id())

search_word = KEY_WORD
count_column = size(split(col("value"), search_word)) - 1

text_file_with_count = text_file_with_index.withColumn("key_word_count", count_column)

filtered_and_sorted = text_file_with_count.filter(col("key_word_count") > 0).orderBy(col("key_word_count").desc())

filtered_and_sorted.select("index", "key_word_count").show(truncate=False)

spark.stop()