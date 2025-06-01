"""
Geospatial helper functions
"""
from shapely.geometry import shape

def clip_to_aoi(raster, aoi_geojson):
    """Clip raster to area of interest"""
    # Implementation using rasterio.mask
    pass

def convert_to_geodataframe(df, lon_col, lat_col):
    """Convert Spark DF to GeoPandas DF"""
    # Implementation with geopandas
    pass
