import unittest
import os
import tempfile
import numpy as np
from forestsentinel.core.preprocessing import DataPreprocessor

try:
    import rasterio
    from rasterio.transform import from_origin
    RASTERIO_AVAILABLE = True
except ImportError:
    RASTERIO_AVAILABLE = False


@unittest.skipIf(not RASTERIO_AVAILABLE, "rasterio not available")
class TestPreprocessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Create a test raster file"""
        cls.temp_dir = tempfile.mkdtemp()
        cls.test_tile_path = os.path.join(cls.temp_dir, "test_tile.tif")
        
        cls.test_config = {
            'data': {
                'processed_dir': cls.temp_dir
            },
            'processing': {
                'cloud_mask': True,
                'indices': ['NDVI']
            }
        }
        
        if RASTERIO_AVAILABLE:
            meta = {
                'driver': 'GTiff',
                'count': 4,
                'dtype': 'float32',
                'width': 100,
                'height': 100,
                'transform': from_origin(0, 0, 1, 1)
            }
            
            with rasterio.open(cls.test_tile_path, 'w', **meta) as dst:
                for i in range(1, 5):
                    dst.write(np.random.rand(100, 100), i)

    def setUp(self):
        self.processor = DataPreprocessor(self.test_config)
        
    def test_ndvi_calculation(self):
        """Test NDVI calculation returns values between -1 and 1"""
        if not RASTERIO_AVAILABLE:
            self.skipTest("rasterio not available")
        ndvi = self.processor.calculate_indices(self.test_tile_path)
        self.assertTrue(np.all((ndvi >= -1) & (ndvi <= 1)))
        
    @classmethod
    def tearDownClass(cls):
        """Clean up test files"""
        if os.path.exists(cls.test_tile_path):
            os.remove(cls.test_tile_path)
        os.rmdir(cls.temp_dir)

if __name__ == '__main__':
    unittest.main()
