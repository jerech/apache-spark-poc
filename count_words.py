from pyspark.sql import SparkSession
from constants import FILE_NAME

# Inicializa una sesión de Spark
spark = SparkSession.builder \
    .appName("Analisis de Texto") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()
#spark = SparkSession.builder \
#    .master("spark://localhost:7077") \
#    .appName("Python-Spark-Docker") \
#    .config("spark.executor.memory", "2g") \
#    .config("spark.executor.cores", "1") \
#    .getOrCreate()


# Lee el archivo de texto como un DataFrame de Spark
text_df = spark.read.text(FILE_NAME)

# Muestra algunas filas del DataFrame
text_df.show()

# Realiza operaciones de transformación y análisis en el DataFrame
word_count_df = text_df.selectExpr("explode(split(value, ' ')) as word") \
    .groupBy("word") \
    .count() \
    .orderBy("count", ascending=False)

# Muestra las palabras más frecuentes
word_count_df.show()

# Detiene la sesión de Spark
spark.stop()
