import unittest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, monotonically_increasing_id

class TestSearchWord(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder \
            .appName("Analisis de Texto Test") \
            .config("spark.executor.memory", "2g") \
            .getOrCreate()
        cls.spark.sparkContext.setLogLevel("ERROR")

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def setUp(self):
        self.file_content = [
            "This is a test line",
            "This line contains the word fraude",
            "Another line without the keyword",
            "fraude appears again in this line"
        ]
        self.search_word = "fraude"
        self.file_name = "test_text_file.txt"

        with open(self.file_name, 'w') as f:
            for line in self.file_content:
                f.write(line + "\n")

    def tearDown(self):
        import os
        os.remove(self.file_name)

    def test_filtered_rows(self):
        text_file = self.spark.read.text(self.file_name)

        text_file_with_index = text_file.withColumn("index", monotonically_increasing_id())

        filtered_rows = text_file_with_index.filter(col("value").contains(self.search_word))

        # Collect the results
        results = filtered_rows.select("index").collect()

        # Verify the results
        expected_indexes = [1, 3]
        actual_indexes = [row["index"] for row in results]

        self.assertEqual(expected_indexes, actual_indexes)

if __name__ == "__main__":
    unittest.main()
