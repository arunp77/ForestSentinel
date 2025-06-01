import unittest
import os
import tempfile
import rasterio
import numpy as np
from forestsentinel.core.preprocessing import DataPreprocessor
from rasterio.transform import from_origin

class TestPreprocessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Create a test raster file"""
        cls.temp_dir = tempfile.mkdtemp()
        cls.test_tile_path = os.path.join(cls.temp_dir, "test_tile.tif")
        
        # Create a mock config dictionary
        cls.test_config = {
            'data': {
                'processed_dir': cls.temp_dir
            },
            'processing': {
                'cloud_mask': True,
                'indices': ['NDVI']
            }
        }
        
        # Create a test raster with 4 bands (Blue, Green, Red, NIR)
        meta = {
            'driver': 'GTiff',
            'count': 4,
            'dtype': 'float32',
            'width': 100,
            'height': 100,
            'transform': from_origin(0, 0, 1, 1)
        }
        
        with rasterio.open(cls.test_tile_path, 'w', **meta) as dst:
            # Write synthetic data
            for i in range(1, 5):
                dst.write(np.random.rand(100, 100), i)

    def setUp(self):
        self.processor = DataPreprocessor(self.test_config)
        
    def test_ndvi_calculation(self):
        """Test NDVI calculation returns values between -1 and 1"""
        ndvi = self.processor.calculate_indices(self.test_tile_path)
        self.assertTrue(np.all((ndvi >= -1) & (ndvi <= 1)))
        
    def test_output_creation(self):
        """Test processed file gets created"""
        output_path = self.processor.process(self.test_tile_path)
        self.assertTrue(os.path.exists(output_path))
        
    @classmethod
    def tearDownClass(cls):
        """Clean up test files"""
        for f in [cls.test_tile_path]:
            if os.path.exists(f):
                os.remove(f)
        os.rmdir(cls.temp_dir)

if __name__ == '__main__':
    unittest.main()
