import unittest
from forestsentinel.core.preprocessing import DataPreprocessor

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        self.processor = DataPreprocessor(test_config)
        
    def test_ndvi_calculation(self):
        test_tile = "tests/data/sample.tif"
        result = self.processor.calculate_indices(test_tile)
        self.assertBetween(result.ndvi, -1, 1)
