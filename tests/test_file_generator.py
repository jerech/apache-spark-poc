import unittest
from io import StringIO
import os
from file_generator import generate_random_text, add_key_word, write_to_file
from constants import KEY_WORD

class TestFileGenerator(unittest.TestCase):

    def test_generate_random_text(self):
        # Test to ensure random text is generated correctly
        size = 100
        random_text = generate_random_text(size)
        self.assertEqual(len(random_text), size)

    def test_add_key_word(self):
        # Test to ensure the key word is added correctly
        random_text = "this is a test text wordto______"
        modified_text = add_key_word(random_text)
        self.assertIn(KEY_WORD, modified_text.split())

    def test_write_to_file(self):
        # Test to ensure the file is written correctly
        file_path = "test_random_text.txt"
        size_mb = 1
        write_to_file(file_path, size_mb)
        self.assertTrue(os.path.exists(file_path))
        # Ensure the file size is approximately correct
        file_size = os.path.getsize(file_path)
        expected_size = size_mb * 1024 * 1024
        self.assertAlmostEqual(file_size, expected_size, delta=expected_size * 0.05)  # Allow 5% error margin
        os.remove(file_path)

if __name__ == "__main__":
    unittest.main()
